from django.conf.urls import url
import django

from sudo import views

if django.VERSION[:3] >= (1, 9, 0):

    urlpatterns = [
        url(r'^sudo/', views.sudo, name='sudo'),
    ]
else:
    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        url(r'^sudo/', 'sudo.views.sudo', name='sudo'),
    )
