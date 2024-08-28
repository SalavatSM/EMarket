from django.urls import path, include
from rest_framework import routers
from .swagger import schema_view


urlpatterns = [
    path('api/', include('shop.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
