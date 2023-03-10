# Generated by Django 4.1.7 on 2023-02-28 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_parts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customeraddress', verbose_name='Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=30, verbose_name='Status')),
                ('auto_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_parts.autopart', verbose_name='Auto part')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderinfo')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['status', 'create_time'],
            },
        ),
    ]
