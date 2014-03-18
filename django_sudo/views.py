"""
django_sudo.views
~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
try:
    from urllib.parse import urlparse, urlunparse
except ImportError:     # Python 2
    from urlparse import urlparse, urlunparse  # noqa

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django_sudo import REDIRECT_FIELD_NAME, REDIRECT_URL
from django_sudo.forms import SudoForm
from django_sudo.utils import grant_sudo_privileges


@sensitive_post_parameters()
@never_cache
@csrf_protect
@login_required
def sudo(request, template_name='sudo.html', extra_context=None):
    redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, REDIRECT_URL)

    if request.is_sudo():
        return HttpResponseRedirect(redirect_to)

    form = SudoForm(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(REDIRECT_URL)
            grant_sudo_privileges(request)
            return HttpResponseRedirect(redirect_to)

    context = {
        'form': form,
        REDIRECT_FIELD_NAME: redirect_to,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context)


def redirect_to_sudo(next_url):
    """
    Redirects the user to the login page, passing the given 'next' page
    """
    sudo_url_parts = list(urlparse(reverse('django_sudo.views.sudo')))

    querystring = QueryDict(sudo_url_parts[4], mutable=True)
    querystring[REDIRECT_FIELD_NAME] = next_url
    sudo_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(sudo_url_parts))
