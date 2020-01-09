#!/usr/bin/env python
"""
django-sudo
~~~~~~~~~~~

:copyright: (c) 2016 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages

install_requires = []

with open("README.md") as f:
    long_description = f.read()


setup(
    name="django-sudo",
    version="3.1.0",
    author="Matt Robenolt",
    author_email="matt@ydekproductions.com",
    url="https://github.com/mattrobenolt/django-sudo",
    description="Extra security for your sensitive pages",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    install_requires=install_requires,
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)
