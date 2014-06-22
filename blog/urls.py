from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
                       url(r'^(?P<post_id>\d+)', views.post),
                       url(r'^page/(?P<page_num>\d+)', views.latest_posts),
                       url(r'^$', views.latest_posts, name='blog'),
)