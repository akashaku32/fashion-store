from django.core.management.base import BaseCommand
from store.models import Category

class Command(BaseCommand):
    help = 'Add sample category images'

    def handle(self, *args, **options):
        # Category images from Unsplash
        category_images = {
            'dresses': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&h=400&fit=crop',
            'tops': 'https://images.unsplash.com/photo-1571513720906-8dd817b4b2d8?w=600&h=400&fit=crop',
            'bottoms': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=600&h=400&fit=crop',
            'outerwear': 'https://images.unsplash.com/photo-1571513720906-8dd817b4b2d8?w=600&h=400&fit=crop',
            'accessories': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&h=400&fit=crop',
            'shoes': 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=600&h=400&fit=crop',
        }

        for category_slug, image_url in category_images.items():
            try:
                category = Category.objects.get(slug=category_slug)
                category.image_url = image_url
                category.save()
                
                self.stdout.write(
                    self.style.SUCCESS(f'Added image for {category.name}')
                )
                
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Category {category_slug} not found')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully added category images!')
        )


