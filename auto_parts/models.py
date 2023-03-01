from audioop import reverse
from django.db import models
from utils.models import BaseModel


class Category(BaseModel):
    name = models.CharField('Category', max_length=50)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class AutoPart(BaseModel):
    category = models.ForeignKey('Category', max_length=30, blank=True,
                                 on_delete=models.PROTECT)
    part_number = models.CharField(max_length=100, blank=True, db_index=True)
    name = models.CharField('Name auto part', max_length=100, db_index=True)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='auto_parts_images/', null=True,
                              blank=True)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2, blank=True)
    available_quantity = models.PositiveIntegerField('Available quantity', default=0)

    def __str__(self) -> str:
        return f"{self.name} {self.part_number}" 
    
    class Meta:
        verbose_name = 'AutoPart'
        verbose_name_plural = 'AutoParts'
        ordering = ['name']
