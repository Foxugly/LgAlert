from django.contrib import admin

from recipient.models import Recipient


class RecipientAdmin(admin.ModelAdmin):
    fields = ['email', 'active']


admin.site.register(Recipient, RecipientAdmin)
