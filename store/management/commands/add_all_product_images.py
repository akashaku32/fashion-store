from django.core.management.base import BaseCommand
from store.models import Product, ProductImage


class Command(BaseCommand):
    help = 'Add comprehensive images to all products for better visual appeal'

    def handle(self, *args, **options):
        self.stdout.write('Adding comprehensive product images...')

        # High-quality product images for each category
        image_library = {
            # Kerala Bridal Products
            'Kanchipuram Bridal Saree - Royal Gold': [
                'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80',
                'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80',
                'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Kerala Kasavu Saree - Pure White': [
                'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80',
                'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Banarasi Silk Bridal Saree': [
                'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Royal Velvet Bridal Lehenga': [
                'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Golden Silk Lehenga Set': [
                'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Pink Rose Bridal Lehenga': [
                'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Traditional Jewelry
            'Kerala Temple Jewelry Set': [
                'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Antique Gold Necklace Set': [
                'https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Wedding Occasion Wear
            'Mehendi Ceremony Anarkali': [
                'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Sangeet Party Sharara': [
                'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Reception Silk Saree': [
                'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Bridal Accessories
            'Kerala Bridal Hair Accessories Set': [
                'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Traditional Bangles Set': [
                'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Elegant Abayas & Modest Wear
            'Royal Black Abaya with Gold Embroidery': [
                'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Emerald Green Kaftan Dress': [
                'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Modest Maxi Dress - Navy Blue': [
                'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Traditional Indian Wear
            'Pink Georgette Salwar Kameez': [
                'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Traditional Punjabi Suit - Royal Blue': [
                'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Cotton Churidar Set - Mustard Yellow': [
                'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Fusion & Contemporary
            'Indo-Western Kurti with Palazzo': [
                'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Contemporary Asymmetric Tunic': [
                'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Party & Festive Wear
            'Sequin Party Gown - Rose Gold': [
                'https://images.unsplash.com/photo-1583391733981-24c87c96b39c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Velvet Festive Anarkali': [
                'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=800&h=1000&fit=crop&auto=format&q=80'
            ],

            # Casual & Everyday
            'Comfortable Cotton Kurta Set': [
                'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&h=1000&fit=crop&auto=format&q=80'
            ],
            'Casual Denim Kurta': [
                'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80'
            ]
        }

        products_updated = 0
        images_added = 0

        for product_name, image_urls in image_library.items():
            try:
                product = Product.objects.get(name=product_name)
                existing_images = product.images.count()

                # Add additional images if needed
                for i, image_url in enumerate(image_urls):
                    if i >= existing_images:  # Only add if we don't have enough images
                        ProductImage.objects.create(
                            product=product,
                            image_url=image_url,
                            alt_text=f'{product.name} - Image {i+1}',
                            is_primary=(i == 0 and existing_images == 0)
                        )
                        images_added += 1

                if existing_images < len(image_urls):
                    products_updated += 1

            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'⚠️ Product not found: {product_name}'))

        # Verify all products have images
        products_without_images = []
        all_products = Product.objects.all()

        for product in all_products:
            if not product.images.exists():
                products_without_images.append(product.name)
                # Add a default image
                ProductImage.objects.create(
                    product=product,
                    image_url='https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=800&h=1000&fit=crop&auto=format&q=80',
                    alt_text=f'{product.name} - Default Image',
                    is_primary=True
                )
                images_added += 1
                products_updated += 1

        self.stdout.write(self.style.SUCCESS(f'✅ Added {images_added} images to {products_updated} products'))
        self.stdout.write(self.style.SUCCESS(f'✅ All {all_products.count()} products now have images'))

        # Final summary
        total_products = all_products.count()
        total_images = ProductImage.objects.count()
        self.stdout.write(f'\n📊 Final Summary:')
        self.stdout.write(f'   🛍️  Total Products: {total_products}')
        self.stdout.write(f'   🖼️  Total Images: {total_images}')
        self.stdout.write(f'   📈 Average Images per Product: {total_images/total_products:.1f}')
