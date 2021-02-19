from django.contrib import admin
from .models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'datetime',
        'description',
        'image',
        'offsite_url',
        'member_only',
    )


admin.site.register(Events, EventsAdmin)

