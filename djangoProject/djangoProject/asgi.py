"""
ASGI config for djangoProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":URLRouter(routings.websocket_urlpatterns)
})