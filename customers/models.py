from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models import BaseModel


class Customer(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=20, db_index=True, unique=True)
    default_address = models.ForeignKey('CustomerAddress', related_name='users', null=True, blank=True,
                                        on_delete=models.SET_NULL, verbose_name='default_address')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['first_name']
        
         
class CustomerAddress(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='addresses',
                                 verbose_name='Addres customer')
    country = models.CharField('Country', max_length=200)
    city = models.CharField('City', max_length=100)
    address = models.CharField('Addres', max_length=100, blank=True)
    
    def __str__(self) -> str:
        return f"{self.customer} {self.country}"
    
    class Meta:
        verbose_name = 'Customer addres'
        verbose_name_plural = verbose_name
        ordering = ['country', 'city']