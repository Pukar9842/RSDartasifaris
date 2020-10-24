from django.contrib import admin
from .  models import DsHome


class DsHomeAdmin(admin.ModelAdmin):
    list_display = ('username', 'userrole', )
admin.site.register(DsHome, DsHomeAdmin)
