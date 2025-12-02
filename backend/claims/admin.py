from django.contrib import admin
from .models import Claim


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'product', 'status', 'priority', 'assigned_to', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description', 'client__name')
    list_editable = ('status', 'priority', 'assigned_to')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Claim Information', {'fields': ('title', 'description', 'client', 'product')}),
        ('Status & Assignment', {'fields': ('status', 'priority', 'assigned_to')}),
        ('Resolution', {'fields': ('resolution_notes', 'resolved_at')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
