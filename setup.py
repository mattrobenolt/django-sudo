#!/usr/bin/env python
"""
django-sudo
~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

install_requires = ['Django']

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-django-lite',
    'flake8',
]


with open('README.rst') as f:
    long_description = f.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        import sys
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='django-sudo',
    version='1.1.3',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/django-sudo',
    description='Extra security for your sensitive pages',
    license='BSD',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    extras_require={
        'tests': tests_require,
    },
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
