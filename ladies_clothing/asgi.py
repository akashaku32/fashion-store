"""
ASGI config for ladies_clothing project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ladies_clothing.settings')

application = get_asgi_application()


