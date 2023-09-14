from django.contrib import admin
from .models import FieldModel, BookingModel


@admin.register(FieldModel)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',  'location', 'is_indoor')
    search_fields = ('name', 'location')


@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('field', 'user', 'start_time', 'end_time', 'is_approved')
    list_filter = ('field', 'user', 'is_approved')
