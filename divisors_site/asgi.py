"""
ASGI config for divisors_site project.
 exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'divisors_site.settings')

application = get_asgi_application()
