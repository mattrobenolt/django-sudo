"""
django_sudo.settings
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django.conf import settings

REDIRECT_URL = getattr(settings, 'SUDO_REDIRECT_URL', '/')
REDIRECT_FIELD_NAME = getattr(settings, 'SUDO_REDIRECT_FIELD_NAME', 'next')
COOKIE_AGE = getattr(settings, 'SUDO_COOKIE_AGE', 10800)
COOKIE_DOMAIN = getattr(settings, 'SUDO_COOKIE_DOMAIN', None)
COOKIE_HTTPONLY = getattr(settings, 'SUDO_COOKIE_HTTPONLY', True)
COOKIE_NAME = getattr(settings, 'SUDO_COOKIE_NAME', 'sudo')
COOKIE_PATH = getattr(settings, 'SUDO_COOKIE_PATH', '/')
COOKIE_SECURE = getattr(settings, 'SUDO_COOKIE_SECURE', None)
