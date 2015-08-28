import django
from django.db import models
try:
    from django.contrib.auth.models import AbstractBaseUser
except ImportError:
    # Django 1.4
    from django.contrib.auth.models import User as AbstractBaseUser


class Django14User(AbstractBaseUser):
    """A Django 1.4-like User object that doesn't have a get_username
    attribute.

    This is only needed so we can test Django 1.4 support, even if a current
    version of Django is installed, and keeping 100% test coverage."""
    def __getattribute__(self, name):
        if name == 'get_username':
            raise AttributeError("%s has no attribute '%s'" % (type(self).__name__, name))
        else:
            return super(Django14User, self).__getattribute__(name)

    username = None


class EmailUser(AbstractBaseUser):
    if django.VERSION >= (1, 5):
        # Skip on Django 1.4, since we're inheriting from User, which already
        # has an email address.
        email = models.CharField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
