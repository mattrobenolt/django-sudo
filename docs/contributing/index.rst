Contributing
============

Getting the source
~~~~~~~~~~~~~~~~~~

You will first want to clone the source repository locally with ``git``:

.. code-block:: console

    $ git clone git@github.com:mattrobenolt/django-sudo.git


Setup Environment
~~~~~~~~~~~~~~~~~

I would recommend using `virtualenv <https://pypi.python.org/pypi/virtualenv>`_ to set up a dev
environment. After creating an environment, install all dep dependencies with:

.. code-block:: console

    $ pip install -e dev-requirements.txt

Running Tests
~~~~~~~~~~~~~

Tests are run using `pytest <https://pypi.python.org/pypi/pytest>`_ and can be found inside
``tests/*``.

Tests can simply be run using:

.. code-block:: console

    $ py.test

This will discover and run the test suite using your default Python interpreter. To run tests
for all supported platforms, we use `tox <https://pypi.python.org/pypi/tox>`_.

.. code-block:: console

    $ tox

Submitting Patches
~~~~~~~~~~~~~~~~~~

Patches are accepted via `Pull Requests <https://github.com/mattrobenolt/django-sudo/pulls>`_ on
GitHub.

.. note::

    If you are submitting a security patch, please see our :doc:`/security/index` page for special
    instructions.

Tests
-----

All new code and changed code must come with **100%** test coverage to be considered for acceptance.
