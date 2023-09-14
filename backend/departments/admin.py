from django.contrib import admin

from .models import Department, DepartmentMember


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(DepartmentMember)
class DepartmentMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'position']
    search_fields = ['user']
    ordering = ['position']
