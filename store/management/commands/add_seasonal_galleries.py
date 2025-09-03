from django.core.management.base import BaseCommand
from django.utils import timezone
from store.models import SeasonalGallery
from datetime import timedelta

class Command(BaseCommand):
    help = 'Adds seasonal gallery images featuring traditional Kerala and Indian cultural fashion'

    def handle(self, *args, **options):
        # Current year for date calculations
        current_year = timezone.now().year

        # Beautiful traditional gallery images
        galleries = [
            # Onam Festival Collection
            {
                'title': 'Onam Festival Special Collection',
                'season': 'onam',
                'style': 'kerala_traditional',
                'description': 'Stunning Kerala kasavu sarees and traditional settu mundu collections for Onam celebration. Features elegant cream and gold combinations with intricate temple borders.',
                'image_url': 'https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=1920&h=1080&fit=crop&auto=format&q=100',
                'start_date': f'{current_year}-08-20',
                'end_date': f'{current_year}-09-05'
            },
            # Wedding Season Collection
            {
                'title': 'Kerala Wedding Elegance',
                'season': 'wedding',
                'style': 'kerala_bridal',
                'description': 'Exquisite bridal collections featuring traditional Kerala wedding sarees, heavily embellished with zari work and temple designs. Perfect for the wedding season.',
                'image_url': 'https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=1920&h=1080&fit=crop&auto=format&q=100',
                'start_date': f'{current_year}-11-01',
                'end_date': f'{current_year}-12-31'
            },
            # Vishu Collection
            {
                'title': 'Vishu Celebration Collection',
                'season': 'vishu',
                'style': 'kerala_traditional',
                'description': 'Welcome the Malayalam New Year with our radiant Vishu collection. Traditional Kerala sarees and settu mundu with contemporary touches.',
                'image_url': 'https://images.unsplash.com/photo-1617038220319-276d3cfab638?w=1920&h=1080&fit=crop&auto=format&q=100',
                'start_date': f'{current_year}-04-01',
                'end_date': f'{current_year}-04-30'
            },
            # Monsoon Collection
            {
                'title': 'Monsoon Magic',
                'season': 'monsoon',
                'style': 'kerala_modern',
                'description': 'Embrace the beauty of Kerala monsoon with our fusion collection. Modern interpretations of traditional designs perfect for the rainy season.',
                'image_url': 'https://images.unsplash.com/photo-1583396060233-3d13c9d7b172?w=1920&h=1080&fit=crop&auto=format&q=100',
                'start_date': f'{current_year}-06-01',
                'end_date': f'{current_year}-08-31'
            },
            # Summer Collection
            {
                'title': 'Summer Ethnic Elegance',
                'season': 'summer',
                'style': 'indo_western',
                'description': 'Light and breezy Indo-western fusion wear perfect for summer. Featuring contemporary takes on traditional Kerala motifs.',
                'image_url': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=1920&h=1080&fit=crop&auto=format&q=100',
                'start_date': f'{current_year}-03-01',
                'end_date': f'{current_year}-05-31'
            },
            # Diwali Collection
            {
                'title': 'Festive Diwali Collection',
                'season': 'diwali',
                'style': 'south_indian',
                'description': 'Celebrate Diwali in style with our festive collection featuring rich silk sarees and contemporary ethnic wear with traditional motifs.',
                'image_url': 'https://images.unsplash.com/photo-1583395838144-09c70d2f7f3c?w=1920&h=1080&fit=crop&auto=format&q=100',
                'start_date': f'{current_year}-10-15',
                'end_date': f'{current_year}-11-15'
            }
        ]

        for gallery_data in galleries:
            gallery, created = SeasonalGallery.objects.update_or_create(
                title=gallery_data['title'],
                defaults={
                    'season': gallery_data['season'],
                    'style': gallery_data['style'],
                    'description': gallery_data['description'],
                    'image_url': gallery_data['image_url'],
                    'start_date': gallery_data['start_date'],
                    'end_date': gallery_data['end_date'],
                    'is_active': True
                }
            )
            
            status = 'Created' if created else 'Updated'
            self.stdout.write(
                self.style.SUCCESS(f'{status} gallery: {gallery.title}')
            )
