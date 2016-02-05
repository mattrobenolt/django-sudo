Changelog
=========

1.3.0
~~~~~
* Store ``redirect_to`` value in session.
  See `#10 <https://github.com/mattrobenolt/django-sudo/pull/10>`_.

1.2.1
~~~~~
* Pass along ``request`` to template context
  See `#8 <https://github.com/mattrobenolt/django-sudo/pull/8>`_.
* Verified compatibility with Django 1.9

1.2.0
~~~~~
* Verified compatibility with python 3.5 and pypy3
* Verified compatibility with Django 1.8
* Dropped support for python 3.2
* Better support for custom User models.
  See `#4 <https://github.com/mattrobenolt/django-sudo/pull/4>`_.
* Added a ``SudoMixin`` for use with class based views.
  See `#5 <https://github.com/mattrobenolt/django-sudo/pull/5>`_.

1.1.3
~~~~~
* Use ``constant_time_compare`` when verifying the correct sudo token.
* Make sure to check against all ``AUTHENTICATION_BACKENDS`` for the ``SudoForm``.
  See `#3 <https://github.com/mattrobenolt/django-sudo/pull/3>`_.

1.1.2
~~~~~
* Added new setting, ``SUDO_FORM`` which allows you to override the default form that is used.
  See `#2 <https://github.com/mattrobenolt/django-sudo/pull/2>`_.

1.1.1
~~~~~
* Fixed a bug when using the new ``SUDO_COOKIE_SALT``.
  If specifying a non-default salt, all cookies would be marked incorrectly
  as invalid.
* Don't use ``request.REQUEST`` anymore since that's deprecated in modern Django.
  Always use ``request.GET`` instead since we never POSTed the ``next`` variable anyways.

1.1.0
~~~~~
* Switch to using signed cookies for the sudo cookie,
  see `#1 <https://github.com/mattrobenolt/django-sudo/issues/1>`_.
* Added new ``SUDO_COOKIE_SALT`` setting to go along with the signed cookie.

1.0.0
~~~~~

* Initial release
