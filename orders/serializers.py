from rest_framework import serializers
from .models import OrderInfo, Order


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
