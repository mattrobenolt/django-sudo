"""
sudo.decorators
~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from functools import wraps

from sudo.views import redirect_to_sudo
import sudo


def sudo_required(func):
    """
    Enforces a view to have elevated privileges.
    Should likely be paired with ``@login_required``.

    >>> @sudo_required
    >>> def secure_page(request):
    >>>     ...
    """
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not request.is_sudo():
            return redirect_to_sudo(request.get_full_path())
        return func(request, *args, **kwargs)
    return inner


def sudo_disabled(func):
    """
    Disables sudo for for a given function to make view
    testing manageable.

    >>> class SomeAppViewsTest(TestCase):
    >>>    @sudo_disabled
    >>>    def test_secure_page(self):
    >>>        ...
    """
    @wraps(func)
    def inner(cls):
        sudo.settings.SUDO_DISABLE = True
        func(cls)
    return inner
