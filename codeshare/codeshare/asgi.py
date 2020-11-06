import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import api.urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeshare.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            api.urls.websocket_urlpatterns
        )
    )
})
