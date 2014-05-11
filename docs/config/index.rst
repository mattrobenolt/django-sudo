Configuration
=============

Settings
~~~~~~~~

By default, all of the settings are optional and define sane and secure defaults.

``SUDO_REDIRECT_URL``
    Default url to be redirected to after elevating permissions. *Default: /*

``SUDO_REDIRECT_FIELD_NAME``
    The querystring argument to be used for redirection. *Default: next*

``SUDO_COOKIE_AGE``
    How long should sudo mode be active for? Duration in seconds. *Default: 10800*

``SUDO_COOKIE_DOMAIN``
    The domain to bind the sudo cookie to. *Default: current exact domain*.

``SUDO_COOKIE_HTTPONLY``
    Should the cookie only be accessible via http requests? *Default: True*

    .. note::
        If this is set to ``False``, any JavaScript files have the ability to access this cookie,
        so this should only be changed if you have a good reason to do so.

``SUDO_COOKIE_NAME``
    The name of the cookie to be used for sudo mode. *Default: sudo*

``SUDO_COOKIE_PATH``
    Restrict the sudo cookie to a specific path. *Default: /*

``SUDO_COOKIE_SECURE``
    Only transmit the sudo cookie over http if True. *Default: matches current protocol*

    .. note::
        By default, we will match the protocol that made the request. So if your sudo page is over
        https, we will set the ``secure`` flag on the cookie so it won't be transmitted over plain
        http. It is highly recommended that you only use ``django-sudo`` over https.

Set up URLs
~~~~~~~~~~~

We need to hook up one url to use ``django-sudo`` properly. At minimum, you need something like
the following:

.. code-block:: python

    (r'^sudo/$',  # Whatever path you want
        'sudo.views.sudo',  # Required
        {'template_name': 'sudo/sudo.html'}  # Optionally change the template to be used
    )

Required Template
~~~~~~~~~~~~~~~~~

To get up and running, we last need to create a template for the sudo page to render. By default,
the package will look for ``sudo/sudo.html`` but can easily be overwritten by setting the
``template_name`` when defining the url definition as seen above.

sudo/sudo.html
--------------

This template gets rendered with the the following context:

``form``
    An instance of :class:`~sudo.forms.SudoForm`.

``SUDO_REDIRECT_FIELD_NAME``
    The value of ``?next=/foo/``. If ``SUDO_REDIRECT_FIELD_NAME`` is ``name``, then expect to find
    ``{{ next }}`` in the context, with the value of ``/foo/``.
