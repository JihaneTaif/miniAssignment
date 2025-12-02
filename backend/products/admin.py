from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'sku', 'description')
    list_editable = ('price', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Product Information', {'fields': ('name', 'description', 'sku')}),
        ('Pricing & Category', {'fields': ('category', 'price', 'is_active')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
