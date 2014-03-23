from .base import BaseTestCase

from django.template.response import TemplateResponse

from django_sudo import REDIRECT_FIELD_NAME, REDIRECT_URL
from django_sudo.views import (
    sudo,
    redirect_to_sudo,
)
from django_sudo.forms import SudoForm


class SudoViewTestCase(BaseTestCase):
    def test_enforces_logged_in(self):
        response = sudo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/accounts/login/?next=/foo')

    def test_returns_template_response(self):
        self.login()
        self.request.is_sudo = lambda: False
        response = sudo(self.request)
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'sudo.html')  # default
        self.assertEqual(response.context_data[REDIRECT_FIELD_NAME], REDIRECT_URL)  # default
        form = response.context_data['form']
        self.assertIsInstance(form, SudoForm)
        self.assertEqual(form.user, self.user)

    def test_returns_template_response_with_next(self):
        self.login()
        self.request.GET = {REDIRECT_FIELD_NAME: '/lol'}
        self.request.is_sudo = lambda: False
        response = sudo(self.request)
        self.assertEqual(response.context_data[REDIRECT_FIELD_NAME], '/lol')  # default

    def test_returns_template_response_override_template(self):
        self.login()
        self.request.is_sudo = lambda: False
        response = sudo(self.request, template_name='foo.html')
        self.assertEqual(response.template_name, 'foo.html')

    def test_returns_template_response_override_extra_context(self):
        self.login()
        self.request.is_sudo = lambda: False
        response = sudo(self.request, extra_context={'foo': 'bar'})
        self.assertEqual(response.context_data['foo'], 'bar')

    def test_redirect_if_already_sudo(self):
        self.login()
        self.request.is_sudo = lambda: True
        response = sudo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], REDIRECT_URL)

    def test_redirect_fix_bad_url(self):
        self.login()
        self.request.is_sudo = lambda: True
        self.request.GET = {REDIRECT_FIELD_NAME: 'http://mattrobenolt.com/lol'}
        response = sudo(self.request)
        self.assertEqual(response['Location'], REDIRECT_URL)

    def test_redirect_if_already_sudo_with_next(self):
        self.login()
        self.request.GET = {REDIRECT_FIELD_NAME: '/lol'}
        self.request.is_sudo = lambda: True
        response = sudo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/lol')

    def test_redirect_after_successful_post(self):
        self.login()
        self.request.is_sudo = lambda: False
        self.request.method = 'POST'
        self.request.csrf_processing_done = True
        self.request.POST = {'password': 'foo'}
        response = sudo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], REDIRECT_URL)

    def test_render_form_with_bad_password(self):
        self.login()
        self.request.is_sudo = lambda: False
        self.request.method = 'POST'
        self.request.csrf_processing_done = True
        self.request.POST = {'password': 'lol'}
        response = sudo(self.request)
        self.assertEqual(response.status_code, 200)
        form = response.context_data['form']
        self.assertFalse(form.is_valid())


class RedirectToSudoTestCase(BaseTestCase):
    def test_redirect_to_sudo_simple(self):
        response = redirect_to_sudo('/foo')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/sudo/?next=/foo')

    def test_redirect_to_sudo_with_querystring(self):
        response = redirect_to_sudo('/foo?foo=bar')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/sudo/?next=/foo%3Ffoo%3Dbar')
