from django.db import models
from utils.models import BaseModel
from customers.models import Customer
from auto_parts.models import AutoPart


class Cart(BaseModel):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                    verbose_name='Customer')
    
  
class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    auto_part_id = models.ForeignKey(AutoPart, on_delete=models.CASCADE,
                                     verbose_name='Auto part number ID')
    quantity = models.PositiveSmallIntegerField('Quantity', default=0)
    
    def __str__(self) -> str:
        return f'Quantity s{self.quantity}, auto part {self.auto_part_id}'

    class Meta:
        verbose_name = 'CartItems'
        verbose_name_plural = verbose_name
        unique_together = ("cart", "auto_part_id")
        ordering = ['-create_time']

    @property
    def total_price(self):
        return self.auto_part_id.price * self.quantity
