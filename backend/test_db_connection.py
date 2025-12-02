import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

from django.db import connection

try:
    cursor = connection.cursor()
    print('✓ Database connection successful!')
    print(f'✓ Connected to: {connection.settings_dict["NAME"]}')
    print(f'✓ Host: {connection.settings_dict["HOST"]}')
    print(f'✓ Database engine: {connection.settings_dict["ENGINE"]}')
except Exception as e:
    print(f'✗ Connection failed: {e}')
