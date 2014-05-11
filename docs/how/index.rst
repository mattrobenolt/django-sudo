How does this work?
===================

``django-sudo`` works by setting an additional cookie that must match a secret value in your
session. This cookie is ideally set to a shorter TTL than the normal session. When not in sudo mode,
any view that is decorated with ``@sudo_required`` will require the user to re-enter their password.
Once in sudo mode, they won't be prompted to enter their password for the next ``SUDO_COOKIE_AGE``
seconds.

In practice, we want to serve this sudo cookie over https only to avoid a man-in-the-middle attack
where someone hijacks this cookie. This can be utilized safely in situations where the sessionid
cookie is being transmitted over http, but we want to make sure that secure areas of our site are
not accessible with just the sessionid.

* When logging in, ``django-sudo`` automatically elevates your permission to ``sudo mode``.
* A second cookie is sent to your browser (by default this cookie is named ``sudo`` but can be set
  to anything with ``SUDO_COOKIE_NAME``). This cookie contains a randomly generated string of
  characters.
* The same randomly generated string of characters is stored in the user's session.
* On subsequent requests, the cookie value must match the value that was stored in the session.
  If the values do not match, or the cookie is not sent at all, the user will be redirected to a
  page to re-enter their password.
* If they re-enter their password successfully, a new cookie is set and their permissions are again
  elevated.

.. note::

    The best way to secure your site and your users is to use https. ``django-sudo`` won't be able
    to help you if it's being served over http.
