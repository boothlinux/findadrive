# Generated by Django 3.2 on 2021-06-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_community', models.CharField(max_length=50)),
            ],
        ),
    ]
