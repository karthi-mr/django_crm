from django.contrib import admin

from webapp.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'creation_date')
    list_display_links = ('first_name',)

admin.site.register(Record, RecordAdmin)