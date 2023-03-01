from rest_framework import viewsets
from .models import Category, AutoPart
from rest_framework.permissions import IsAuthenticated
from .serializers import SerializerAutoPart, SerializerCategory


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = SerializerCategory

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AutoPart.objects.all()
    serializer_class = SerializerAutoPart
    

