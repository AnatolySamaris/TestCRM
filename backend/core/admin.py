from django.contrib import admin

from django.contrib.auth.models import Group
from .models import User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ('username', 'name', 'email', "password")}),
        (None, {"fields": ('last_login', 'date_joined')}),
        (None, {"fields": ('is_active', 'is_superuser', 'is_staff')})
    )
    list_display = ['username', 'email']
    exclude = ['groups', 'user_permissions']
