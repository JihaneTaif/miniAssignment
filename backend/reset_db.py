import os
import django
from django.conf import settings
from django.db import connection

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

def reset_db():
    print("🗑️  Dropping all tables...")
    with connection.cursor() as cursor:
        cursor.execute("""
            DO $$ DECLARE
                r RECORD;
            BEGIN
                FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                END LOOP;
            END $$;
        """)
    print("✅ All tables dropped.")

if __name__ == '__main__':
    reset_db()
