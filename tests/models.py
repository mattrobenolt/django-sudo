import django
from django.db import models
try:
    from django.contrib.auth.models import AbstractBaseUser
except ImportError:
    # Django 1.4 doesn't properly support custom user models, but a User is
    # close enough to AbstractBaseUser for our tests to work in 1.4.
    from django.contrib.auth.models import User as AbstractBaseUser


class EmailUser(AbstractBaseUser):
    if django.VERSION >= (1, 5):
        # Skip on Django 1.4, since we're inheriting from User, which already
        # has an email address.
        email = models.CharField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    class Meta:
        app_label = 'sudo_tests'
