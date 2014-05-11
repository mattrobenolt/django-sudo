Usage
=====

Once we have ``django-sudo`` :doc:`installed </getting-started/index>` and
:doc:`configured </config/index>`, we need to decide which views should be secured.

.. function:: sudo.decorators.sudo_required()

    The meat of ``django-sudo`` comes from decorating your views with ``@sudo_required`` much in the
    same way that ``@login_required`` works.

    Let's pretend that we have a page on our site that has sensitive information that we want to make
    extra sure that a user is allowed to see it:

    .. code-block:: python

        from sudo.decorators import sudo_required

        @login_required  # Make sure they're at least logged in
        @sudo_required  # On top of being logged in, are you in sudo mode?
        def super_secret_stuff(request):
            return HttpResponse('your social security number')

    That's it! When a user visits this page and they don't have the correct permission, they'll be
    redirected to a page and prompted for their password. After entering their password, they'll be
    redirected back to this page to continue on what they were trying to do.

.. method:: request.is_sudo()

Returns a boolean to indicate if the current request is in sudo mode or not. This gets added on by
the :class:`~sudo.middleware.SudoMiddleware`. This is an shortcut for calling
:func:`~sudo.utils.has_sudo_privileges` directly.

.. class:: sudo.middleware.SudoMiddleware

    By default, you just need to add this into your ``MIDDLEWARE_CLASSES`` list.

    .. method:: has_sudo_privileges(self, request)
    
    Subclass and override :func:`~sudo.middleware.SudoMiddleware.has_sudo_privileges` if you'd like
    to override the default behavior of :func:`request.is_sudo() <request.is_sudo()>`.

    .. method:: process_request(self, request)

    Adds :func:`~request.is_sudo()` to the request.

    .. method:: process_response(self, request, response)

    Controls the behavior of setting and deleting the sudo cookie for the browser.


.. module:: sudo.utils

.. function:: grant_sudo_privileges(request, max_age=SUDO_COOKIE_AGE)

    Assigns a random token to the user's session that allows them to have elevated permissions.

    .. code-block:: python

        from sudo.utils import grant_sudo_privileges
        token = grant_sudo_privileges(request)

.. function:: revoke_sudo_privileges(request)

    Revoke sudo privileges from a request explicitly

    .. code-block:: python

        from sudo.utils import revoke_sudo_privileges
        revoke_sudo_privileges(request)

.. function:: has_sudo_privileges(request)

    Check if a request is allowed to perform sudo actions.

    .. code-block:: python

        from sudo.utils import has_sudo_privileges
        has_sudo = has_sudo_privileges(request)
