from rest_framework import serializers
from .models import Customer, CustomerAddress


class AdressCustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerAddress
        fields = '__all__'
        
        
class CustomerSerializer(serializers.ModelSerializer):
    default_address = AdressCustomerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'