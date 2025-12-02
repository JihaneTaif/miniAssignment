from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'account_manager', 'created_at')
    list_filter = ('created_at', 'industry')
    search_fields = ('name', 'email', 'company')
    readonly_fields = ('created_at', 'updated_at', 'converted_from_lead')
    
    fieldsets = (
        ('Contact Information', {'fields': ('name', 'email', 'phone', 'company', 'address')}),
        ('Business Details', {'fields': ('industry', 'account_manager', 'notes')}),
        ('Conversion', {'fields': ('converted_from_lead',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
