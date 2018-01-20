from django.conf.urls import include, url
from django.contrib import admin

from frontpage import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^blog/', include('blog.urls')),
               url(r'^admin/', include(admin.site.urls)),
               ]

    # Examples:
    # url(r'^$', 'personalsite.views.home', name='home'),
    # url(r'^personalsite/', include('personalsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
