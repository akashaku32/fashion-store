#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ladies_clothing.settings')
django.setup()

from django.contrib.auth.models import User

# Check existing users first
print("=== CHECKING EXISTING USERS ===")
all_users = User.objects.all()
print(f"Total users: {all_users.count()}")

if all_users.exists():
    print("\nExisting users:")
    for user in all_users:
        status = []
        if user.is_superuser:
            status.append("SUPERUSER")
        if user.is_staff:
            status.append("STAFF")
        if user.is_active:
            status.append("ACTIVE")
        
        status_str = ", ".join(status) if status else "REGULAR USER"
        print(f"  - {user.username} ({user.email}) - {status_str}")

print("\n=== CREATING SUPERUSER ===")

# Superuser credentials
username = 'admin'
email = 'admin@lunandlace.com'
password = 'admin123'

# Check if superuser already exists
if User.objects.filter(username=username).exists():
    print(f"User '{username}' already exists!")
    existing_user = User.objects.get(username=username)
    if existing_user.is_superuser:
        print(f"'{username}' is already a superuser!")
    else:
        print(f"Making '{username}' a superuser...")
        existing_user.is_superuser = True
        existing_user.is_staff = True
        existing_user.save()
        print("✅ User upgraded to superuser!")
else:
    # Create new superuser
    print(f"Creating new superuser '{username}'...")
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("✅ Superuser created successfully!")
    except Exception as e:
        print(f"❌ Error creating superuser: {e}")

print(f"\n=== ADMIN ACCESS ===")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Admin URL: http://127.0.0.1:8000/admin/")
print(f"Make sure your Django server is running!")

