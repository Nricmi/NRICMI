from django.contrib import admin
from .models import Notification

# Register your models here.
from .models import PageContent
admin.site.register(PageContent)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')
    search_fields = ('message',)