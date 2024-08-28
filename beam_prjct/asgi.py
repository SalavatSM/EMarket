import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import shop.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beam_prjct.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            shop.routing.websocket_urlpatterns
        )
    ),
})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beam_prjct.settings')

application = get_asgi_application()
