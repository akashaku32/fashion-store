#!/usr/bin/env python
"""
Setup script for Elegance Boutique Django project
"""
import os
import sys
import subprocess


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def main():
    """Main setup function"""
    print("=" * 60)
    print("Elegance Boutique - Django E-commerce Setup")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("Failed to install requirements. Please check your Python environment.")
        sys.exit(1)
    
    # Make migrations
    if not run_command("python manage.py makemigrations", "Creating database migrations"):
        print("Failed to create migrations.")
        sys.exit(1)
    
    # Apply migrations
    if not run_command("python manage.py migrate", "Applying database migrations"):
        print("Failed to apply migrations.")
        sys.exit(1)
    
    # Create superuser (optional)
    print("\n" + "=" * 60)
    print("Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Create a superuser account:")
    print("   python manage.py createsuperuser")
    print("\n2. Populate with sample data (optional):")
    print("   python manage.py populate_data")
    print("\n3. Start the development server:")
    print("   python manage.py runserver")
    print("\n4. Access the website at: http://127.0.0.1:8000/")
    print("   Admin panel at: http://127.0.0.1:8000/admin/")
    print("\nDemo credentials (if you ran populate_data):")
    print("   Username: demo")
    print("   Password: demo123")


if __name__ == "__main__":
    main()


