from django.db import models
from customers.models import Customer, CustomerAddress
from auto_parts.models import AutoPart
from utils.models import BaseModel


class OrderInfo(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 db_index=True, verbose_name='Customer')
    address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE,
                                verbose_name='Address')
 
    def __str__(self) -> str:
        return f"{self.customer} {self.address}"


STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)


class Order(BaseModel):
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE,)
    phone = models.CharField('Phone', max_length=30)
    auto_part = models.ForeignKey(AutoPart, on_delete=models.CASCADE,
                                  verbose_name='Auto part')
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(choices=STATUS_CHOICES, default='Pending',
                              max_length=30, verbose_name='Status')

    def __str__(self) -> str:
        return f"{self.order.customer} - {self.auto_part}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['status', 'create_time']
