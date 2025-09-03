from django.core.management.base import BaseCommand
from store.models import Product, ProductImage
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Add sample product images'

    def handle(self, *args, **options):
        # Create sample image URLs (you can replace these with actual image files)
        sample_images = {
            'elegant-evening-dress': [
                'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=600&fit=crop',
                'https://images.unsplash.com/photo-1566479179817-c0d9de9a8a2a?w=400&h=600&fit=crop',
            ],
            'wool-blend-coat': [
                'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=600&fit=crop',
                'https://images.unsplash.com/photo-1571513720906-8dd817b4b2d8?w=400&h=600&fit=crop',
            ],
            'leather-handbag': [
                'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=600&fit=crop',
                'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400&h=600&fit=crop',
            ],
            'classic-black-heels': [
                'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400&h=600&fit=crop',
                'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&h=600&fit=crop',
            ],
            'floral-summer-dress': [
                'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=600&fit=crop',
                'https://images.unsplash.com/photo-1571513720906-8dd817b4b2d8?w=400&h=600&fit=crop',
            ],
            'silk-scarf': [
                'https://images.unsplash.com/photo-1601925260369-5b0b5b5b5b5b?w=400&h=600&fit=crop',
                'https://images.unsplash.com/photo-1601925260369-5b0b5b5b5b5b?w=400&h=600&fit=crop',
            ],
        }

        for product_slug, image_urls in sample_images.items():
            try:
                product = Product.objects.get(slug=product_slug)
                
                # Clear existing images
                product.images.all().delete()
                
                # Add new images
                for i, image_url in enumerate(image_urls):
                    ProductImage.objects.create(
                        product=product,
                        image_url=image_url,
                        alt_text=f"{product.name} - Image {i+1}",
                        is_primary=(i == 0)
                    )
                
                self.stdout.write(
                    self.style.SUCCESS(f'Added images for {product.name}')
                )
                
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Product {product_slug} not found')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully added product images!')
        )
