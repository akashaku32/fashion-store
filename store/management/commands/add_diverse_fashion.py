from django.core.management.base import BaseCommand
from store.models import Category, Product, ProductImage
from decimal import Decimal


class Command(BaseCommand):
    help = 'Add diverse cultural fashion styles - Kerala, Islamic, Traditional Indian, Western, and Fusion wear'

    def handle(self, *args, **options):
        self.stdout.write('Adding diverse cultural fashion collection...')

        # Create diverse categories
        diverse_categories_data = [
            {
                'name': 'Elegant Abayas & Modest Wear',
                'description': 'Beautiful modest fashion including abayas, kaftans, and elegant modest dresses',
                'image_url': 'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Traditional Indian Wear',
                'description': 'Stunning salwar kameez, churidars, and traditional Indian outfits for all occasions',
                'image_url': 'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Fusion & Contemporary',
                'description': 'Modern fusion wear blending traditional and contemporary styles',
                'image_url': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Party & Festive Wear',
                'description': 'Glamorous outfits for celebrations, parties, and festive occasions',
                'image_url': 'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Casual & Everyday',
                'description': 'Comfortable and stylish everyday wear with cultural touches',
                'image_url': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=600&fit=crop&auto=format&q=80'
            }
        ]

        categories = {}
        for cat_data in diverse_categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'slug': cat_data['name'].lower().replace(' ', '-').replace('&', 'and'),
                    'image_url': cat_data['image_url'],
                    'is_active': True
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Diverse Fashion Products
        diverse_products = [
            # Elegant Abayas & Modest Wear
            {
                'name': 'Royal Black Abaya with Gold Embroidery',
                'description': 'Elegant black abaya with intricate gold embroidery and flowing silhouette, perfect for formal occasions and daily wear.',
                'category': 'Elegant Abayas & Modest Wear',
                'price': Decimal('8999.00'),
                'discount_price': Decimal('6999.00'),
                'size': 'L',
                'color': 'Black',
                'stock_quantity': 15,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Emerald Green Kaftan Dress',
                'description': 'Flowing emerald green kaftan with beautiful prints, comfortable and elegant for any occasion.',
                'category': 'Elegant Abayas & Modest Wear',
                'price': Decimal('5999.00'),
                'discount_price': Decimal('4499.00'),
                'size': 'M',
                'color': 'Green',
                'stock_quantity': 20,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Modest Maxi Dress - Navy Blue',
                'description': 'Beautiful modest maxi dress in navy blue with elegant sleeves and flowing design.',
                'category': 'Elegant Abayas & Modest Wear',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3999.00'),
                'size': 'S',
                'color': 'Blue',
                'stock_quantity': 18,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Traditional Indian Wear
            {
                'name': 'Pink Georgette Salwar Kameez',
                'description': 'Beautiful pink georgette salwar kameez with thread work and traditional Indian styling.',
                'category': 'Traditional Indian Wear',
                'price': Decimal('7999.00'),
                'discount_price': Decimal('5999.00'),
                'size': 'M',
                'color': 'Pink',
                'stock_quantity': 12,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Traditional Punjabi Suit - Royal Blue',
                'description': 'Elegant royal blue Punjabi suit with traditional phulkari embroidery and matching dupatta.',
                'category': 'Traditional Indian Wear',
                'price': Decimal('9999.00'),
                'discount_price': Decimal('7999.00'),
                'size': 'L',
                'color': 'Blue',
                'stock_quantity': 10,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Cotton Churidar Set - Mustard Yellow',
                'description': 'Comfortable cotton churidar set in mustard yellow with block prints and traditional styling.',
                'category': 'Traditional Indian Wear',
                'price': Decimal('3999.00'),
                'discount_price': Decimal('2999.00'),
                'size': 'S',
                'color': 'Yellow',
                'stock_quantity': 25,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Fusion & Contemporary
            {
                'name': 'Indo-Western Kurti with Palazzo',
                'description': 'Modern indo-western kurti paired with palazzo pants, perfect blend of traditional and contemporary.',
                'category': 'Fusion & Contemporary',
                'price': Decimal('6999.00'),
                'discount_price': Decimal('5499.00'),
                'size': 'M',
                'color': 'Purple',
                'stock_quantity': 16,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Contemporary Asymmetric Tunic',
                'description': 'Stylish asymmetric tunic with modern cuts and traditional prints, versatile for multiple occasions.',
                'category': 'Fusion & Contemporary',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3999.00'),
                'size': 'L',
                'color': 'Orange',
                'stock_quantity': 14,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Party & Festive Wear
            {
                'name': 'Sequin Party Gown - Rose Gold',
                'description': 'Glamorous rose gold sequin gown perfect for parties, weddings, and special celebrations.',
                'category': 'Party & Festive Wear',
                'price': Decimal('15999.00'),
                'discount_price': Decimal('12999.00'),
                'size': 'M',
                'color': 'Pink',
                'stock_quantity': 8,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Velvet Festive Anarkali',
                'description': 'Rich velvet Anarkali with golden work, perfect for festivals and grand celebrations.',
                'category': 'Party & Festive Wear',
                'price': Decimal('18999.00'),
                'discount_price': Decimal('14999.00'),
                'size': 'L',
                'color': 'Red',
                'stock_quantity': 6,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Casual & Everyday
            {
                'name': 'Comfortable Cotton Kurta Set',
                'description': 'Soft cotton kurta set with traditional prints, perfect for daily wear and casual outings.',
                'category': 'Casual & Everyday',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('2299.00'),
                'size': 'M',
                'color': 'White',
                'stock_quantity': 30,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Casual Denim Kurta',
                'description': 'Modern denim kurta with traditional collar and styling, perfect for casual college and office wear.',
                'category': 'Casual & Everyday',
                'price': Decimal('3499.00'),
                'discount_price': Decimal('2699.00'),
                'size': 'S',
                'color': 'Blue',
                'stock_quantity': 22,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            }
        ]

        # Create products
        for product_data in diverse_products:
            category = categories[product_data['category']]
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'slug': product_data['name'].lower().replace(' ', '-').replace(',', '').replace("'", '').replace('&', 'and'),
                    'category': category,
                    'price': product_data['price'],
                    'discount_price': product_data.get('discount_price'),
                    'size': product_data['size'],
                    'color': product_data['color'],
                    'stock_quantity': product_data['stock_quantity'],
                    'is_featured': product_data['is_featured'],
                    'is_active': True
                }
            )
            
            if created:
                # Add product images
                for i, image_url in enumerate(product_data['images']):
                    ProductImage.objects.create(
                        product=product,
                        image_url=image_url,
                        alt_text=f'{product.name} - Image {i+1}',
                        is_primary=(i == 0)
                    )
                
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(self.style.SUCCESS('✅ Successfully added diverse cultural fashion collection!'))
        self.stdout.write(f'Total categories: {Category.objects.count()}')
        self.stdout.write(f'Total products: {Product.objects.count()}')
