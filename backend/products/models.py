from django.db import models


class Product(models.Model):
    """Product/Service model"""
    
    CATEGORY_CHOICES = [
        ('product', 'Product'),
        ('service', 'Service'),
        ('subscription', 'Subscription'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True, db_index=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'products'
        ordering = ['name']
        indexes = [
            models.Index(fields=['category', 'is_active']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.sku})"
