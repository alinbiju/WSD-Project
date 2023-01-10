# Generated by Django 4.0.3 on 2022-04-13 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Bus_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=50, verbose_name='bus_name')),
                ('departure', models.CharField(max_length=20, verbose_name='departure')),
                ('destination', models.CharField(blank=True, max_length=20, verbose_name='destination')),
                ('duration', models.CharField(max_length=10, verbose_name='duration')),
                ('departure_time', models.CharField(blank=True, max_length=50, verbose_name='departure_time')),
                ('arrival', models.CharField(blank=True, max_length=10, verbose_name='arrival')),
                ('price', models.CharField(max_length=10, verbose_name='price')),
                ('seat_left', models.CharField(max_length=10, verbose_name='seat_left')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='city_name')),
                ('city_pincode', models.IntegerField(verbose_name='city_pincode')),
            ],
        ),
        migrations.CreateModel(
            name='Flights_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=50, verbose_name='flight_name')),
                ('departure', models.CharField(max_length=20, verbose_name='departure')),
                ('destination', models.CharField(blank=True, max_length=20, verbose_name='destination')),
                ('duration', models.CharField(max_length=10, verbose_name='duration')),
                ('departure_time', models.CharField(blank=True, max_length=50, verbose_name='departure_time')),
                ('arrival', models.CharField(blank=True, max_length=10, verbose_name='arrival')),
                ('price', models.CharField(max_length=10, verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50, verbose_name='hotel_name')),
                ('image', models.ImageField(default='insert image', upload_to='images/')),
                ('image2', models.ImageField(default='insert image', upload_to='images/')),
                ('image3', models.ImageField(default='insert image', upload_to='images/')),
                ('price', models.IntegerField(default=4900, verbose_name='price')),
                ('check_in', models.CharField(max_length=10, verbose_name='check_in')),
                ('check_out', models.CharField(max_length=10, verbose_name='check_out')),
                ('hotel_details', models.CharField(max_length=1000, verbose_name='hotel_details')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50, verbose_name='state_name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Package_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_name', models.CharField(max_length=50, verbose_name='pack_name')),
                ('destination', models.CharField(default='AaBbCc', max_length=50, verbose_name='destination')),
                ('pack_details', models.CharField(max_length=300, verbose_name='pack_details')),
                ('pack_price', models.IntegerField(verbose_name='pack_price')),
                ('image', models.ImageField(upload_to='images/')),
                ('image1', models.ImageField(default='asda', upload_to='images/')),
                ('image2', models.ImageField(default='asda', upload_to='images/')),
                ('image3', models.ImageField(default='asda', upload_to='images/')),
                ('days', models.CharField(default='1', max_length=10, verbose_name='days')),
                ('nights', models.CharField(default='1', max_length=10, verbose_name='nights')),
                ('city_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
                ('state_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='Package_Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=0, verbose_name='day')),
                ('hotel_img', models.ImageField(default='asda', upload_to='images/')),
                ('hotel_name', models.CharField(default='asda', max_length=50, verbose_name='hotel_name')),
                ('sightseeing', models.CharField(blank=True, max_length=40, verbose_name='sightseeing')),
                ('sightseeing1', models.CharField(blank=True, max_length=40, verbose_name='sightseeing1')),
                ('sightseeing2', models.CharField(blank=True, max_length=40, verbose_name='sightseeing2')),
                ('sightseeing3', models.CharField(blank=True, max_length=40, verbose_name='sightseeing3')),
                ('meal', models.CharField(default='2', max_length=20, verbose_name='meal')),
                ('hotel_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel_master')),
                ('package_master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.package_master')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50, verbose_name='room_name')),
                ('room_type_1', models.CharField(blank=True, max_length=50, verbose_name='room_type_1')),
                ('room_type_2', models.CharField(blank=True, max_length=50, verbose_name='room_type_2')),
                ('max_guest_1', models.CharField(blank=True, max_length=50, verbose_name='max_guest_1')),
                ('max_guest_2', models.CharField(blank=True, max_length=50, verbose_name='max_guest_2')),
                ('amenities_1', models.CharField(blank=True, max_length=15, verbose_name='amenities_1')),
                ('amenities_2', models.CharField(blank=True, max_length=15, verbose_name='amenities_2')),
                ('amenities_3', models.CharField(blank=True, max_length=15, verbose_name='amenities_3')),
                ('amenities_4', models.CharField(blank=True, max_length=15, verbose_name='amenities_4')),
                ('amenities_5', models.CharField(blank=True, max_length=15, verbose_name='amenities_5')),
                ('inclusions_type_1_1', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_1_1')),
                ('inclusions_type_1_2', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_1_2')),
                ('inclusions_type_1_3', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_1_3')),
                ('inclusions_type_1_4', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_1_4')),
                ('inclusions_type_1_5', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_1_5')),
                ('inclusions_type_2_1', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_2_1')),
                ('inclusions_type_2_2', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_2_2')),
                ('inclusions_type_2_3', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_2_3')),
                ('inclusions_type_2_4', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_2_4')),
                ('inclusions_type_2_5', models.CharField(blank=True, max_length=35, verbose_name='inclusions_type_2_5')),
                ('highlights_type_1_1', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_1_1')),
                ('highlights_type_1_2', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_1_2')),
                ('highlights_type_1_3', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_1_3')),
                ('highlights_type_1_4', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_1_4')),
                ('highlights_type_1_5', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_1_5')),
                ('highlights_type_2_1', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_2_1')),
                ('highlights_type_2_2', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_2_2')),
                ('highlights_type_2_3', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_2_3')),
                ('highlights_type_2_4', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_2_4')),
                ('highlights_type_2_5', models.CharField(blank=True, max_length=65, verbose_name='highlights_type_2_5')),
                ('room_price_type_1', models.IntegerField(blank=True, verbose_name='room_price_type_1')),
                ('room_price_type_2', models.IntegerField(blank=True, verbose_name='room_price_type_2')),
                ('image_1', models.ImageField(default='Insert Image', upload_to='image/')),
                ('hotel_master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel_master')),
            ],
        ),
        migrations.AddField(
            model_name='hotel_master',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
        migrations.CreateModel(
            name='Booking_Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30, verbose_name='fullname')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('state', models.CharField(max_length=30, verbose_name='state')),
                ('zipcode', models.CharField(max_length=30, verbose_name='zipcode')),
                ('rooms', models.IntegerField(verbose_name='rooms')),
                ('price', models.IntegerField(verbose_name='price')),
                ('adults', models.IntegerField(default=2, verbose_name='adults')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel_master')),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.package_master')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30, verbose_name='fullname')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('city', models.CharField(max_length=30, verbose_name='city')),
                ('state', models.CharField(max_length=30, verbose_name='state')),
                ('zipcode', models.CharField(max_length=30, verbose_name='zipcode')),
                ('rooms', models.IntegerField(verbose_name='rooms')),
                ('price', models.IntegerField(verbose_name='price')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hotel_master')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]