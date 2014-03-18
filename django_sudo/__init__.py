"""
django_sudo
~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django.conf import settings

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django_sudo').version
except Exception as e:
    VERSION = 'unknown'


REDIRECT_URL = getattr(settings, 'SUDO_REDIRECT_URL', '/')
REDIRECT_FIELD_NAME = getattr(settings, 'SUDO_REDIRECT_FIELD_NAME', 'next')
COOKIE_NAME = getattr(settings, 'SUDO_COOKIE_NAME', 'sudo')
COOKIE_MAX_AGE = getattr(settings, 'SUDO_COOKIE_MAX_AGE', 10800)
