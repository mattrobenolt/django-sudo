Getting Started
===============

Installation
~~~~~~~~~~~~

First, install the ``django-sudo`` library with `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: console

    $ pip install django-sudo

Next, we need to add the ``sudo`` application to our ``INSTALLED_APPS``. Installing the application
will automatically register the ``user_logged_in`` and ``user_logged_out`` signals that are needed.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'sudo',
    )

Now we need to install the required middleware into ``MIDDLEWARE``:

.. code-block:: python

    MIDDLEWARE = (
        # ...
        'sudo.middleware.SudoMiddleware',
    )

.. note::

    ``sudo.middleware.SudoMiddleware`` **must** be installed after
    ``django.contrib.session.middleware.SessionMiddleware``.

Proceed to the :doc:`/config/index` documentation.
