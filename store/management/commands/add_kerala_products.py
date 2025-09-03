from django.core.management.base import BaseCommand
from store.models import Category, Product, ProductImage
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Add Kerala wedding and bridal products to the store'

    def handle(self, *args, **options):
        self.stdout.write('Adding Kerala wedding and bridal products...')

        # Create Kerala-specific categories
        kerala_categories_data = [
            {
                'name': 'Kerala Bridal Sarees',
                'description': 'Traditional Kerala bridal sarees with gold borders and rich silk',
                'image_url': 'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Wedding Lehengas',
                'description': 'Stunning bridal lehengas with intricate embroidery and vibrant colors',
                'image_url': 'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Kerala Traditional Jewelry',
                'description': 'Authentic Kerala gold jewelry including temple jewelry and antique designs',
                'image_url': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Wedding Occasion Wear',
                'description': 'Beautiful outfits for wedding ceremonies, mehendi, and sangeet',
                'image_url': 'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=600&fit=crop&auto=format&q=80'
            },
            {
                'name': 'Bridal Accessories',
                'description': 'Complete bridal accessories including hair ornaments and bangles',
                'image_url': 'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=600&fit=crop&auto=format&q=80'
            }
        ]

        categories = {}
        for cat_data in kerala_categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'slug': cat_data['name'].lower().replace(' ', '-'),
                    'image_url': cat_data['image_url'],
                    'is_active': True
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Kerala Bridal Products
        kerala_products = [
            # Kerala Bridal Sarees
            {
                'name': 'Kanchipuram Bridal Saree - Royal Gold',
                'description': 'Exquisite Kanchipuram silk saree with heavy gold zari work, traditional temple border, and rich red color perfect for Kerala brides.',
                'category': 'Kerala Bridal Sarees',
                'price': Decimal('45999.00'),
                'discount_price': Decimal('38999.00'),
                'size': 'L',
                'color': 'Red',
                'stock_quantity': 8,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80',
                    'https://images.unsplash.com/photo-1596462008713-dc4f7b8b1d3b?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Kerala Kasavu Saree - Pure White',
                'description': 'Traditional Kerala kasavu saree with authentic gold border, handwoven in pure cotton for wedding ceremonies.',
                'category': 'Kerala Bridal Sarees',
                'price': Decimal('12999.00'),
                'discount_price': Decimal('9999.00'),
                'size': 'M',
                'color': 'White',
                'stock_quantity': 15,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Banarasi Silk Bridal Saree',
                'description': 'Luxurious Banarasi silk saree with intricate brocade work and peacock motifs, perfect for South Indian brides.',
                'category': 'Kerala Bridal Sarees',
                'price': Decimal('35999.00'),
                'discount_price': Decimal('29999.00'),
                'size': 'L',
                'color': 'Purple',
                'stock_quantity': 6,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Wedding Lehengas
            {
                'name': 'Royal Velvet Bridal Lehenga',
                'description': 'Stunning velvet lehenga with heavy embroidery, sequin work, and traditional Kerala motifs in rich maroon color.',
                'category': 'Wedding Lehengas',
                'price': Decimal('65999.00'),
                'discount_price': Decimal('55999.00'),
                'size': 'M',
                'color': 'Red',
                'stock_quantity': 4,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Golden Silk Lehenga Set',
                'description': 'Elegant golden silk lehenga with intricate thread work, perfect for Kerala wedding ceremonies and receptions.',
                'category': 'Wedding Lehengas',
                'price': Decimal('48999.00'),
                'discount_price': Decimal('42999.00'),
                'size': 'S',
                'color': 'Yellow',
                'stock_quantity': 7,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Pink Rose Bridal Lehenga',
                'description': 'Beautiful pink lehenga with floral embroidery, mirror work, and traditional Kerala design elements.',
                'category': 'Wedding Lehengas',
                'price': Decimal('39999.00'),
                'discount_price': Decimal('34999.00'),
                'size': 'M',
                'color': 'Pink',
                'stock_quantity': 9,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Traditional Jewelry
            {
                'name': 'Kerala Temple Jewelry Set',
                'description': 'Authentic Kerala temple jewelry set with Lakshmi pendant, traditional earrings, and antique gold finish.',
                'category': 'Kerala Traditional Jewelry',
                'price': Decimal('25999.00'),
                'discount_price': Decimal('22999.00'),
                'size': 'S',
                'color': 'Yellow',
                'stock_quantity': 12,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Antique Gold Necklace Set',
                'description': 'Traditional Kerala antique gold necklace with matching earrings, perfect for bridal occasions.',
                'category': 'Kerala Traditional Jewelry',
                'price': Decimal('18999.00'),
                'discount_price': Decimal('15999.00'),
                'size': 'M',
                'color': 'Yellow',
                'stock_quantity': 8,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Wedding Occasion Wear
            {
                'name': 'Mehendi Ceremony Anarkali',
                'description': 'Vibrant green Anarkali suit with floral embroidery, perfect for mehendi and pre-wedding ceremonies.',
                'category': 'Wedding Occasion Wear',
                'price': Decimal('8999.00'),
                'discount_price': Decimal('6999.00'),
                'size': 'M',
                'color': 'Green',
                'stock_quantity': 20,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Sangeet Party Sharara',
                'description': 'Glamorous sharara set with sequin work and mirror embellishments, ideal for sangeet and cocktail parties.',
                'category': 'Wedding Occasion Wear',
                'price': Decimal('15999.00'),
                'discount_price': Decimal('12999.00'),
                'size': 'L',
                'color': 'Blue',
                'stock_quantity': 14,
                'is_featured': True,
                'images': [
                    'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Reception Silk Saree',
                'description': 'Elegant silk saree with contemporary design and traditional Kerala elements for wedding receptions.',
                'category': 'Wedding Occasion Wear',
                'price': Decimal('11999.00'),
                'discount_price': Decimal('9999.00'),
                'size': 'M',
                'color': 'Orange',
                'stock_quantity': 16,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },

            # Bridal Accessories
            {
                'name': 'Kerala Bridal Hair Accessories Set',
                'description': 'Complete set of traditional Kerala bridal hair ornaments including jadanagam, chandra, and fresh flower alternatives.',
                'category': 'Bridal Accessories',
                'price': Decimal('5999.00'),
                'discount_price': Decimal('4999.00'),
                'size': 'S',
                'color': 'Yellow',
                'stock_quantity': 25,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            },
            {
                'name': 'Traditional Bangles Set',
                'description': 'Authentic Kerala-style gold bangles with traditional patterns and antique finish.',
                'category': 'Bridal Accessories',
                'price': Decimal('7999.00'),
                'discount_price': Decimal('6999.00'),
                'size': 'M',
                'color': 'Yellow',
                'stock_quantity': 30,
                'is_featured': False,
                'images': [
                    'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=1000&fit=crop&auto=format&q=80'
                ]
            }
        ]

        # Create products
        for product_data in kerala_products:
            category = categories[product_data['category']]
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'slug': product_data['name'].lower().replace(' ', '-').replace(',', '').replace("'", ''),
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

        self.stdout.write(self.style.SUCCESS('✅ Successfully added Kerala wedding and bridal products!'))
        self.stdout.write(f'Total categories: {Category.objects.count()}')
        self.stdout.write(f'Total products: {Product.objects.count()}')
