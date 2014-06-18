from django.contrib import admin
from frontpage.models import Data

__author__ = 'nate'


class DataAdmin(admin.ModelAdmin):
    pass
admin.site.register(Data, DataAdmin)
