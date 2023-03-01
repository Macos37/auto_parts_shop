from django.urls import path, include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]