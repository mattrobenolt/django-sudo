"""
django_sudo.signals
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from django_sudo.utils import grant_sudo_privileges, revoke_sudo_privileges


@receiver(user_logged_in)
def grant(sender, request, **kwargs):
    grant_sudo_privileges(request)


@receiver(user_logged_out)
def revoke(sender, request, **kwargs):
    revoke_sudo_privileges(request)
