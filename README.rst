django-sudo
===========

.. image:: https://travis-ci.org/mattrobenolt/django-sudo.svg?branch=master
   :target: https://travis-ci.org/mattrobenolt/django-sudo

.. image:: https://coveralls.io/repos/mattrobenolt/django-sudo/badge.png?branch=master
   :target: https://coveralls.io/r/mattrobenolt/django-sudo?branch=master

..

    | Sudo mode is an extra layer of security for your most sensitive pages.
    This is an implementation of GitHub's `Sudo Mode
    <https://github.com/blog/1513-introducing-github-sudo-mode>`_ for `Django
    <https://www.djangoproject.com/>`_.

What is this for?
~~~~~~~~~~~~~~~~~
``django-sudo`` provides an extra layer of security for after a user is already logged in. Views can
be decorated with ``@sudo_required``, and then a user
must re-enter their password to view that page. After verifying their password, that user has
elevated permissions for the duration of ``SUDO_COOKIE_AGE``. This duration is independent of the
normal session duration allowing short elevated permission durations, but retain long user sessions.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install django-sudo

Compatibility
~~~~~~~~~~~~~
* Django 1.4-1.9
* Python 2.6-3.5
* pypy

Resources
~~~~~~~~~
* `Documentation <https://django-sudo.readthedocs.org/>`_
* `Security <https://django-sudo.readthedocs.org/en/latest/security/index.html>`_
* `Changelog <https://django-sudo.readthedocs.org/en/latest/changelog/index.html>`_
