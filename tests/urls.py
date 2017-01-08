import django

from sudo import views

if django.VERSION[:3] >= (1, 9, 0):
    from django.conf.urls import url

    urlpatterns = [
        url(r'^sudo/', views.sudo, name='sudo'),
    ]
else:
    try:
        from django.conf.urls import url, patterns
    except ImportError:
        from django.conf.urls.defaults import url, patterns  # noqa


    urlpatterns = patterns(
        '',
        url(r'^sudo/', 'sudo.views.sudo', name='sudo'),
    )
