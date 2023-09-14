from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "deadline", "hours_cost"]
    search_fields = ["title"]
    ordering = ["created_at"]