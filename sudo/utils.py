"""
sudo.utils
~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
import unicodedata

from django.core.signing import BadSignature
from django.utils import six
from django.utils.crypto import get_random_string, constant_time_compare
from django.utils.encoding import force_text
from django.utils.six.moves.urllib.parse import urlparse

from sudo.settings import COOKIE_NAME, COOKIE_AGE, COOKIE_SALT


def grant_sudo_privileges(request, max_age=COOKIE_AGE):
    """
    Assigns a random token to the user's session
    that allows them to have elevated permissions
    """
    user = getattr(request, 'user', None)

    # If there's not a user on the request, just noop
    if user is None:
        return

    if not user.is_authenticated():
        raise ValueError('User needs to be logged in to be elevated to sudo')

    # Token doesn't need to be unique,
    # just needs to be unpredictable and match the cookie and the session
    token = get_random_string()
    request.session[COOKIE_NAME] = token
    request._sudo = True
    request._sudo_token = token
    request._sudo_max_age = max_age
    return token


def revoke_sudo_privileges(request):
    """
    Revoke sudo privileges from a request explicitly
    """
    request._sudo = False
    if COOKIE_NAME in request.session:
        del request.session[COOKIE_NAME]


def has_sudo_privileges(request):
    """
    Check if a request is allowed to perform sudo actions
    """
    if getattr(request, '_sudo', None) is None:
        try:
            request._sudo = (
                request.user.is_authenticated() and
                constant_time_compare(
                    request.get_signed_cookie(COOKIE_NAME, salt=COOKIE_SALT, max_age=COOKIE_AGE),
                    request.session[COOKIE_NAME]
                )
            )
        except (KeyError, BadSignature):
            request._sudo = False
    return request._sudo


def is_safe_url(url, host=None):
    """
    Return ``True`` if the url is a safe redirection (i.e. it doesn't point to
    a different host and uses a safe scheme).
    Always returns ``False`` on an empty url.
    """
    if url is not None:
        url = url.strip()
    if not url:
        return False
    if six.PY2:  # pragma: nocover
        try:
            url = force_text(url)
        except UnicodeDecodeError:
            return False
    # Chrome treats \ completely as / in paths but it could be part of some
    # basic auth credentials so we need to check both URLs.
    return _is_safe_url(url, host) and _is_safe_url(url.replace('\\', '/'), host)


def _is_safe_url(url, host):
    # Chrome considers any URL with more than two slashes to be absolute, but
    # urlparse is not so flexible. Treat any url with three slashes as unsafe.
    if url.startswith('///'):
        return False
    url_info = urlparse(url)
    # Forbid URLs like http:///example.com - with a scheme, but without a hostname.
    # In that URL, example.com is not the hostname but, a path component. However,
    # Chrome will still consider example.com to be the hostname, so we must not
    # allow this syntax.
    if not url_info.netloc and url_info.scheme:
        return False
    # Forbid URLs that start with control characters. Some browsers (like
    # Chrome) ignore quite a few control characters at the start of a
    # URL and might consider the URL as scheme relative.
    if unicodedata.category(url[0])[0] == 'C':
        return False
    return ((not url_info.netloc or url_info.netloc == host) and
            (not url_info.scheme or url_info.scheme in ('http', 'https')))
