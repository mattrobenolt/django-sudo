"""
sudo.views
~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
try:
    from urllib.parse import urlparse, urlunparse
except ImportError:  # pragma: no cover
    # Python 2 fallback
    from urlparse import urlparse, urlunparse  # noqa

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, QueryDict
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.utils.decorators import method_decorator

from sudo.settings import (REDIRECT_FIELD_NAME, REDIRECT_URL,
                           REDIRECT_TO_FIELD_NAME, URL)
from sudo.utils import grant_sudo_privileges
from sudo.forms import SudoForm

try:
    from django.shortcuts import resolve_url
except ImportError:  # pragma: no cover
    # Django <1.5 doesn't have `resolve_url`
    from django.core import urlresolvers

    # resolve_url yanked from Django 1.5.5
    def resolve_url(to, *args, **kwargs):
        """
        Return a URL appropriate for the arguments passed.

        The arguments could be:

            * A model: the model's `get_absolute_url()` function will be called.

            * A view name, possibly with arguments: `urlresolvers.reverse()` will
              be used to reverse-resolve the name.

            * A URL, which will be returned as-is.

        """
        # If it's a model, use get_absolute_url()
        if hasattr(to, 'get_absolute_url'):
            return to.get_absolute_url()

        # Next try a reverse URL resolution.
        try:
            return urlresolvers.reverse(to, args=args, kwargs=kwargs)
        except urlresolvers.NoReverseMatch:
            # If this is a callable, re-raise.
            if callable(to):
                raise
            # If this doesn't "feel" like a URL, re-raise.
            if '/' not in to and '.' not in to:
                raise

        # Finally, fall back and assume it's a URL
        return to


class SudoView(View):
    """
    The default view for the sudo mode page. The role of this page is to
    prompt the user for their password again, and if successful, redirect
    them back to ``next``.
    """
    form_class = SudoForm
    template_name = 'sudo/sudo.html'
    extra_context = None

    def handle_sudo(self, request, redirect_to, context):
        return request.method == 'POST' and context['form'].is_valid()

    def grant_sudo_privileges(self, request, redirect_to):
        grant_sudo_privileges(request)
        # Restore the redirect destination from the GET request
        redirect_to = request.session.pop(REDIRECT_TO_FIELD_NAME,
                                          redirect_to)
        # Double check we're not redirecting to other sites
        if not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = resolve_url(REDIRECT_URL)
        return HttpResponseRedirect(redirect_to)

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, request):
        redirect_to = request.GET.get(REDIRECT_FIELD_NAME, REDIRECT_URL)

        # Make sure we're not redirecting to other sites
        if not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = resolve_url(REDIRECT_URL)

        if request.is_sudo():
            return HttpResponseRedirect(redirect_to)

        if request.method == 'GET':
            request.session[REDIRECT_TO_FIELD_NAME] = redirect_to

        context = {
            'form': self.form_class(request.user, request.POST or None),
            'request': request,
            REDIRECT_FIELD_NAME: redirect_to,
        }
        if self.handle_sudo(request, redirect_to, context):
            return self.grant_sudo_privileges(request, redirect_to)
        if self.extra_context is not None:
            context.update(self.extra_context)
        return TemplateResponse(request, self.template_name, context)


def sudo(request, **kwargs):
    return SudoView(**kwargs).dispatch(request)


def redirect_to_sudo(next_url, sudo_url=None):
    """
    Redirects the user to the login page, passing the given 'next' page
    """
    if sudo_url is None:
        sudo_url = URL

    sudo_url_parts = list(urlparse(resolve_url(sudo_url)))

    querystring = QueryDict(sudo_url_parts[4], mutable=True)
    querystring[REDIRECT_FIELD_NAME] = next_url
    sudo_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(sudo_url_parts))
