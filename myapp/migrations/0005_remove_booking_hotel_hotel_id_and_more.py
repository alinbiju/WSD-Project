# Generated by Django 4.0.3 on 2022-04-13 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_booking_package_price_booking_package_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_hotel',
            name='hotel_id',
        ),
        migrations.RemoveField(
            model_name='booking_hotel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='booking_hotel',
            name='user_id',
        ),
    ]