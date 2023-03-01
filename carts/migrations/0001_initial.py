# Generated by Django 4.1.7 on 2023-02-28 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_parts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')),
                ('auto_part_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_parts.autopart', verbose_name='Auto part number ID')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'ordering': ['-create_time'],
            },
        ),
    ]
