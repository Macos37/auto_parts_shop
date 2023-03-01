from rest_framework import viewsets
from .models import Cart, CartItems
from .serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)
        return queryset

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemSerializer