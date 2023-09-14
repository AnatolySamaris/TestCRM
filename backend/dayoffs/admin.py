from django.contrib import admin

from .models import Application, Dayoff


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(Dayoff)
class DayoffAdmin(admin.ModelAdmin):
    list_display = ["user", "date_from", "date_to"]
    search_fields = ["user"]
