Changelog
=========

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
