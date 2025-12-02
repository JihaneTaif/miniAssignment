from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'status', 'source', 'assigned_to', 'created_at')
    list_filter = ('status', 'source', 'created_at')
    search_fields = ('name', 'email', 'company')
    list_editable = ('status', 'assigned_to')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Contact Information', {'fields': ('name', 'email', 'phone', 'company')}),
        ('Lead Details', {'fields': ('status', 'source', 'assigned_to', 'notes')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
