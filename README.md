# django-sudo

[![](https://travis-ci.org/mattrobenolt/django-sudo.svg?branch=master)](https://travis-ci.org/mattrobenolt/django-sudo) [![](https://coveralls.io/repos/mattrobenolt/django-sudo/badge.png?branch=master)](https://coveralls.io/r/mattrobenolt/django-sudo?branch=master)

> Sudo mode is an extra layer of security for your most sensitive pages.<br>
> This is an implementation of GitHub's [Sudo Mode](https://github.com/blog/1513-introducing-github-sudo-mode) for [Django](https://www.djangoproject.com/).

## What is this for?

`django-sudo` provides an extra layer of security for after a user is already logged in. Views can
be decorated with `@sudo_required`, and then a user
must re-enter their password to view that page. After verifying their password, that user has
elevated permissions for the duration of `SUDO_COOKIE_AGE`. This duration is independent of the
normal session duration allowing short elevated permission durations, but retain long user sessions.

## Installation

```console
$ pip install django-sudo
```

## Compatibility

* Django 1.9-1.11
* Python 2.7, 3.6-3.7

## Resources

* [Documentation](https://django-sudo.readthedocs.io/)
* [Security](https://django-sudo.readthedocs.io/en/latest/security/index.html)
* [Changelog](https://django-sudo.readthedocs.io/en/latest/changelog/index.html)
