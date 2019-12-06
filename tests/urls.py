from __future__ import absolute_import

try:
    from django.conf.urls import url, patterns
except ImportError:
    from django.conf.urls.defaults import url, patterns  # noqa


urlpatterns = patterns(
    '',
    url(r'^sudo/', 'sudo.views.sudo', name='sudo'),
)
