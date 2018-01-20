from django.conf.urls import include, url
# django default account login page
from django.contrib.auth import views as auth_views

from ping import views

urlpatterns = [
        url(r'^accounts/login/$',
            auth_views.LoginView.as_view(template_name='ping/login.html')),
        url(r'^test_view/$', views.test_view)]
