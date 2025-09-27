from django.contrib import admin
from .models import DeviceToken

@admin.register(DeviceToken)
class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "platform", "active", "created_at")
    list_filter = ("platform", "active")
    search_fields = ("user__username", "token")
