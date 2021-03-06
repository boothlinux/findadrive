# Generated by Django 3.2 on 2021-06-04 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_community'),
        ('passenger', '0002_alter_riderequest_completed_ride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderequest',
            name='completed_ride',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='riderequest',
            name='dropoff_town',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dropoff_town', to='driver.community'),
        ),
        migrations.AlterField(
            model_name='riderequest',
            name='pickup_town',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pickup_town', to='driver.community'),
        ),
    ]
