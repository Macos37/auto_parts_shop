from rest_framework.response import Response
from rest_framework import viewsets
from .models import CustomerAddress, Customer
from .serializers import AdressCustomerSerializer, CustomerSerializer


class AddressCustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = AdressCustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'count': queryset.count(),
            'results': serializer.data
        }
        return Response(data)