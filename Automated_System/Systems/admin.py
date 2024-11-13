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


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_price', 'service_duration', 'service_category']
    list_filter = ['service_category']
    search_fields = ['service_name', 'service_category']
    fieldsets = [
        ('Service Information', {'fields': ['service_name', 'service_description', 'service_price', 'service_duration', 'service_image', 'service_category']})
    ]
    ordering = ['service_name']


@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ['user', 'service', 'appointment_date', 'appointment_time', 'appointment_status', 'appointment_created']
    list_filter = ['appointment_status']
    search_fields = ['user', 'service', 'appointment_date', 'appointment_time']
    fieldsets = [
        ('Appointment Information', {'fields': ['user', 'service', 'appointment_date', 'appointment_time', 'appointment_status']})
    ]
    ordering = ['appointment_date', 'appointment_time']
    list_select_related = ['user', 'service']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_message', 'notification_created']
    search_fields = ['user', 'notification_message']
    fieldsets = [
        ('Notification Information', {'fields': ['user', 'notification_message']})
    ]
    ordering = ['notification_created']
    list_select_related = ['user']