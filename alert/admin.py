from django.contrib import admin

from alert.models import Alert


class AlertAdmin(admin.ModelAdmin):
    fields = ['created', 'title', 'content']


admin.site.register(Alert, AlertAdmin)
