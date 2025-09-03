"""
WSGI config for ladies_clothing project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ladies_clothing.settings')

application = get_wsgi_application()


