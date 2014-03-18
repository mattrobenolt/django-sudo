#!/usr/bin/env python
"""
django-sudo
~~~~~~~~~~~

Sudo mode.

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages

setup(
    name='django-sudo',
    version='0.0.2',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/django-sudo',
    description='Sudo mode',
    license='BSD',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'Django',
    ],
    py_modules=['django_sudo'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
