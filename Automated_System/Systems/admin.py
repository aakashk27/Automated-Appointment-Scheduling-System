from django.contrib import admin
from Systems.models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_customer', 'is_admin']
    list_filter = ['is_customer', 'is_admin']
    search_fields = ['username', 'email', 'phone_number']
    fieldsets = [
        ('User Information', {'fields': ['username', 'email', 'phone_number', 'password']}),
        ('Permissions', {'fields': ['is_customer', 'is_admin']})
    ]
    add_fieldsets = [
        ('User Information', {'fields': ['username', 'email', 'phone_number', 'password1', 'password2']}),
        ('Permissions', {'fields': ['is_customer', 'is_admin']})
    ]
    ordering = ['username']