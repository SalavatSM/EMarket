from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('api/', include('shop.api.urls')),
    path('swagger/', get_schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', get_schema_view().with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
