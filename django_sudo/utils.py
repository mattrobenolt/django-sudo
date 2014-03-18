"""
django_sudo.utils
~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django.utils.crypto import get_random_string

from django_sudo import COOKIE_NAME, COOKIE_MAX_AGE


def grant_sudo_privileges(request, max_age=COOKIE_MAX_AGE):
    """
    Assigns a random token to the user's session that allows them to have elevated permissions
    """
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
                request.COOKIES[COOKIE_NAME] == request.session[COOKIE_NAME]
            )
        except KeyError:
            request._sudo = False
    return request._sudo
