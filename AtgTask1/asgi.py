"""
ASGI config for AtgTask1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import PublicChatRoom.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AtgTask1.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(PublicChatRoom.routing.websocket_urlpatterns)
    )
})

