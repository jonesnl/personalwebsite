from django.conf.urls import include, url

from blog import views

urlpatterns = [url(r'^(?P<post_id>\d+)', views.post),
               url(r'^page/(?P<page_num>\d+)', views.latest_posts),
               url(r'^$', views.latest_posts, name='blog'),
               ]
