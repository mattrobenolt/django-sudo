"""
sudo.forms
~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django import forms
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _


class SudoForm(forms.Form):
    """
    A simple password input form used by the default :func:`~sudo.views.sudo` view.
    """
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SudoForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        try:
            username = self.user.get_username()   # Django 1.5 and above
        except AttributeError:                    # pragma: nocover
            username = self.user.username         # Django 1.4
        if auth.authenticate(username=username, password=self.data['password']):
            return self.data['password']
        raise forms.ValidationError(_('Incorrect password'))
