from django.conf.urls import include, url
# django default account login page
from django.contrib.auth import views as auth_views

from ping import views

urlpatterns = [
        url(r'^accounts/login/$',
            auth_views.LoginView.as_view(template_name='ping/login.html'), name='login'),
        url(r'^accounts/logout/$',
            auth_views.LogoutView.as_view(template_name='ping/logout.html'), name='logout'),
        url(r'^$', views.test_view, name='ping')]
