from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<algorithm_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.paste_algo, name='paste_algo'),
]