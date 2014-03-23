from .base import BaseTestCase

from django.http import HttpResponse
from django_sudo.decorators import sudo_required


@sudo_required
def foo(request):
    return HttpResponse()


class SudoRequiredTestCase(BaseTestCase):
    def test_is_sudo(self):
        self.request.is_sudo = lambda: True
        response = foo(self.request)
        self.assertEqual(response.status_code, 200)

    def test_is_not_sudo(self):
        self.request.is_sudo = lambda: False
        response = foo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/sudo/?next=/foo')
