from django.urls import path, include
from rest_framework import routers
from ..views import UserViewSet, ProductViewSet, CategoryViewSet, OrderViewSet, AddressViewSet

from rest_framework.response import Response


def root_view(request):
    return Response({'message': 'API is running'})


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', root_view),
    path('', include(router.urls)),
    path('users/', UserViewSet.as_view({'get': 'list'}))
]

