from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import os

from . import urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeo.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            urls.websocket_urlpatterns
        )
    )
})