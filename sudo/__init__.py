"""
sudo
~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sudo').version
except Exception:  # pragma: no cover
    VERSION = 'unknown'
