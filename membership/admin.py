from django.contrib import admin
from .models import Membership

class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'expiry',
        'is_premium'
    )

admin.site.register(Membership, MembershipAdmin)
