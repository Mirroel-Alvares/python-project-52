from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from task_manager.statuses.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ["name"]
    list_filter = [("created_at", DateFieldListFilter)]
