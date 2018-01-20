from django.contrib import admin
from ping.models import Ping

# Register your models here.

class PingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ping, PingAdmin)
