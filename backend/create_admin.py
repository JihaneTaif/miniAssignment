"""
Script to create a default admin user for the ERP system
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create admin user if it doesn't exist
if not User.objects.filter(email='admin@erp.com').exists():
    User.objects.create_superuser(
        email='admin@erp.com',
        password='admin123',
        first_name='Admin',
        last_name='User',
        role='admin'
    )
    print('✓ Admin user created successfully!')
    print('  Email: admin@erp.com')
    print('  Password: admin123')
else:
    print('Admin user already exists')
