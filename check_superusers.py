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

def check_superusers():
    print("🔍 Checking for existing users in the database...\n")
    
    # Get all users
    all_users = User.objects.all()
    
    if not all_users.exists():
        print("❌ No users found in the database.")
        print("\n💡 To create a superuser, run:")
        print("   python manage.py createsuperuser")
        return
    
    print(f"📊 Total users in database: {all_users.count()}")
    print("\n👥 User Details:")
    print("-" * 80)
    print(f"{'ID':<5} {'Username':<15} {'Email':<25} {'Staff':<8} {'Superuser':<10} {'Active':<8}")
    print("-" * 80)
    
    for user in all_users:
        print(f"{user.id:<5} {user.username:<15} {user.email:<25} {'Yes' if user.is_staff else 'No':<8} {'Yes' if user.is_superuser else 'No':<10} {'Yes' if user.is_active else 'No':<8}")
    
    # Check specifically for superusers
    superusers = User.objects.filter(is_superuser=True)
    
    if superusers.exists():
        print(f"\n🔐 Found {superusers.count()} superuser(s):")
        for su in superusers:
            print(f"   • Username: {su.username}")
            print(f"     Email: {su.email}")
            print(f"     Active: {'Yes' if su.is_active else 'No'}")
        print(f"\n🌐 Access admin panel at: http://127.0.0.1:8000/admin/")
    else:
        print("\n❌ No superusers found!")
        print("\n💡 Create a superuser by running one of these commands:")
        print("   1. python manage.py createsuperuser")
        print("   2. python create_simple_superuser.py (if you want automated creation)")

if __name__ == '__main__':
    check_superusers()

