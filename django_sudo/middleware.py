"""
django_sudo.middleware
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django_sudo import COOKIE_NAME
from django_sudo.utils import has_sudo_privileges


class SudoMiddleware(object):
    def has_sudo_privileges(self, request):
        ## Override me to alter behavior
        return has_sudo_privileges(request)

    def process_request(self, request):
        assert hasattr(request, 'session'), 'django_sudo depends on SessionMiddleware!'

        request.is_sudo = lambda: self.has_sudo_privileges(request)

    def process_response(self, request, response):
        is_sudo = getattr(request, '_sudo', None)

        if is_sudo is None:
            return response

        # We have explicitly had sudo revoked, so clean up cookie
        if is_sudo is False and COOKIE_NAME in request.COOKIES:
            response.delete_cookie(COOKIE_NAME)
            return response

        # Sudo mode has been granted, and we have a token to send back to the user agent
        if is_sudo is True and hasattr(request, '_sudo_token'):
            token = request._sudo_token
            max_age = request._sudo_max_age
            response.set_cookie(
                COOKIE_NAME, token,
                max_age=max_age,  # If max_age is None, it's a session cookie
                secure=request.is_secure(),
                httponly=True,  # Not accessible by JavaScript
            )

        return response
