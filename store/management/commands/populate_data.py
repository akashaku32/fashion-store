from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product, ProductImage, Customer
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {'name': 'Dresses', 'description': 'Elegant dresses for every occasion'},
            {'name': 'Tops & Blouses', 'description': 'Stylish tops and blouses'},
            {'name': 'Bottoms', 'description': 'Pants, skirts, and shorts'},
            {'name': 'Outerwear', 'description': 'Jackets, coats, and cardigans'},
            {'name': 'Accessories', 'description': 'Bags, jewelry, and scarves'},
            {'name': 'Shoes', 'description': 'Heels, flats, and boots'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'slug': cat_data['name'].lower().replace(' ', '-').replace('&', 'and'),
                }
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create sample products
        products_data = [
            {
                'name': 'Elegant Evening Dress',
                'description': 'A stunning evening dress perfect for special occasions. Features a flattering silhouette and luxurious fabric.',
                'category': 'Dresses',
                'price': Decimal('299.99'),
                'discount_price': Decimal('249.99'),
                'size': 'M',
                'color': 'Black',
                'stock_quantity': 15,
                'is_featured': True,
            },
            {
                'name': 'Classic White Blouse',
                'description': 'A timeless white blouse that pairs perfectly with any outfit. Made from premium cotton.',
                'category': 'Tops & Blouses',
                'price': Decimal('89.99'),
                'size': 'L',
                'color': 'White',
                'stock_quantity': 25,
                'is_featured': True,
            },
            {
                'name': 'High-Waisted Jeans',
                'description': 'Comfortable and stylish high-waisted jeans with a perfect fit. Made from premium denim.',
                'category': 'Bottoms',
                'price': Decimal('129.99'),
                'discount_price': Decimal('99.99'),
                'size': 'S',
                'color': 'Blue',
                'stock_quantity': 20,
            },
            {
                'name': 'Wool Blend Coat',
                'description': 'A warm and stylish wool blend coat perfect for winter. Features a classic design.',
                'category': 'Outerwear',
                'price': Decimal('399.99'),
                'size': 'M',
                'color': 'Navy',
                'stock_quantity': 10,
                'is_featured': True,
            },
            {
                'name': 'Leather Handbag',
                'description': 'A premium leather handbag with multiple compartments. Perfect for everyday use.',
                'category': 'Accessories',
                'price': Decimal('199.99'),
                'size': 'One Size',
                'color': 'Brown',
                'stock_quantity': 30,
            },
            {
                'name': 'Classic Black Heels',
                'description': 'Elegant black heels that add sophistication to any outfit. Comfortable for all-day wear.',
                'category': 'Shoes',
                'price': Decimal('159.99'),
                'discount_price': Decimal('129.99'),
                'size': '8',
                'color': 'Black',
                'stock_quantity': 18,
                'is_featured': True,
            },
            {
                'name': 'Floral Summer Dress',
                'description': 'A beautiful floral dress perfect for summer days. Light and airy fabric.',
                'category': 'Dresses',
                'price': Decimal('179.99'),
                'size': 'S',
                'color': 'Pink',
                'stock_quantity': 22,
            },
            {
                'name': 'Silk Scarf',
                'description': 'A luxurious silk scarf with a beautiful pattern. Adds elegance to any outfit.',
                'category': 'Accessories',
                'price': Decimal('79.99'),
                'size': 'One Size',
                'color': 'Purple',
                'stock_quantity': 40,
            },
        ]

        for product_data in products_data:
            category = next(cat for cat in categories if cat.name == product_data['category'])
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'category': category,
                    'price': product_data['price'],
                    'discount_price': product_data.get('discount_price'),
                    'size': product_data['size'],
                    'color': product_data['color'],
                    'stock_quantity': product_data['stock_quantity'],
                    'is_featured': product_data.get('is_featured', False),
                    'slug': product_data['name'].lower().replace(' ', '-'),
                }
            )
            
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create a sample user and customer
        if not User.objects.filter(username='demo').exists():
            user = User.objects.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123',
                first_name='Demo',
                last_name='User'
            )
            customer = Customer.objects.create(user=user, phone='+1234567890')
            self.stdout.write('Created demo user: demo/demo123')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )


