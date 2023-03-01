from rest_framework import serializers
from .models import AutoPart, Category

class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SerializerAutoPart(serializers.ModelSerializer):
    category = SerializerCategory()
    
    class Meta:
        model = AutoPart
        fields = '__all__'




