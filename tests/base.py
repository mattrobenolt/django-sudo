try:
    from django.utils import unittest
except ImportError:
    import unittest

from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.request = self.get('/foo')
        self.request.session = {}
        self.request.COOKIES = {}
        self.setUser(AnonymousUser())

    def get(self, *args, **kwargs):
        return RequestFactory().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return RequestFactory().post(*args, **kwargs)

    def setUser(self, user):
        self.user = self.request.user = user

    def login(self):
        user = User()
        user.set_password('foo')
        self.setUser(user)
