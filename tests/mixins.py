from .base import BaseTestCase
from django.http import HttpResponse
from django.views import generic
from sudo.mixins import SudoMixin


class FooView(SudoMixin, generic.View):
    def get(self, request):
        return HttpResponse()

foo = FooView.as_view()


class SudoMixinTestCase(BaseTestCase):
    def test_is_sudo(self):
        self.request.is_sudo = lambda: True
        response = foo(self.request)
        self.assertEqual(response.status_code, 200)

    def test_is_not_sudo(self):
        self.request.is_sudo = lambda: False
        response = foo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/sudo/?next=/foo')
