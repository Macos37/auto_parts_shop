from rest_framework import serializers
from .models import Cart, CartItems
from auto_parts.serializers import SerializerAutoPart

class CartItemSerializer(serializers.ModelSerializer):
    product = SerializerAutoPart()

    class Meta:
        model = CartItems
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
