from django.urls import re_path
from .consumers import MyConsumer

websocket_urlpatterns = [
    re_path(r'ws/myconsumer', MyConsumer.as_asgi()),
]