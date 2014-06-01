from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
                       url(r'^(?P<post_id>\d+)', views.post),
                       url(r'^latest$', views.latest_post),
                       url(r'^$', views.latest_post, name='blog'),
)