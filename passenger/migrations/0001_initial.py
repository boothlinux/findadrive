# Generated by Django 3.2 on 2021-06-04 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('home_town', models.CharField(max_length=50)),
                ('home_postal_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_town', models.CharField(max_length=50)),
                ('pickup_street_address', models.CharField(max_length=50)),
                ('pickup_postal_code', models.CharField(max_length=7)),
                ('dropoff_town', models.CharField(max_length=50)),
                ('dropoff_street_address', models.CharField(max_length=50)),
                ('dropoff_postal_code', models.CharField(max_length=7)),
                ('comments', models.CharField(max_length=1024)),
                ('accepted_ride', models.BooleanField(default=False)),
                ('rejected_ride_comments', models.CharField(blank=True, max_length=1024)),
                ('completed_ride', models.BooleanField(default=True)),
                ('passenger', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='passenger.passenger')),
            ],
        ),
    ]
