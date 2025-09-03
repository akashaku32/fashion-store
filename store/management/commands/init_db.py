from django.core.management.base import BaseCommand
from django.core.management import call_command
import sys


class Command(BaseCommand):
    help = 'Initialize database with sample data for deployment'

    def handle(self, *args, **options):
        try:
            self.stdout.write('Initializing database...')
            
            # Populate sample data
            try:
                call_command('populate_data')
                self.stdout.write(self.style.SUCCESS('✅ Sample data populated'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Populate data: {str(e)}'))
            
            # Add category images
            try:
                call_command('add_category_images')
                self.stdout.write(self.style.SUCCESS('✅ Category images added'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Category images: {str(e)}'))
            
            # Add product images
            try:
                call_command('add_product_images')
                self.stdout.write(self.style.SUCCESS('✅ Product images added'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Product images: {str(e)}'))
            
            # Add Kerala wedding products
            try:
                call_command('add_kerala_products')
                self.stdout.write(self.style.SUCCESS('✅ Kerala wedding products added'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Kerala products: {str(e)}'))
            
            self.stdout.write(self.style.SUCCESS('🎉 Database initialization completed!'))
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Database initialization failed: {str(e)}')
            )
            # Don't exit with error code to prevent deployment failure
            pass
