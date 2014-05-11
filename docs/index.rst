Welcome to ``django-sudo``
==========================

``django-sudo`` is an implementation of GitHub's `Sudo Mode
<https://github.com/blog/1513-introducing-github-sudo-mode>`_ for `Django
<https://www.djangoproject.com/>`_.

What is this for?
~~~~~~~~~~~~~~~~~
``django-sudo`` provides an extra layer of security for after a user is already logged in. Views can
be decorated with :func:`@sudo_required <django_sudo.decorators.sudo_required>`, and then a user
must re-enter their password to view that page. After verifying their password, that user has
elevated permissions for the duration of ``SUDO_COOKIE_AGE``. This duration is independent of the
normal session duration allowing short elevated permission durations, but retain long user sessions.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install django-sudo

Contents
~~~~~~~~

.. toctree::
   :maxdepth: 2

   getting-started/index
   config/index
   usage/index
   contributing/index
   how/index
   security/index
   changelog/index
