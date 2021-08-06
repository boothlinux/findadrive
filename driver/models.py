from django.db import models
from passenger.models import RideRequest

# Create your models here.

class Community(models.Model):
    name_of_community = models.CharField(max_length=50)

    def __str__(self):
        print(self.name_of_community)
        return str(self.name_of_community)

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    insured = models.BooleanField(default=True)

    def __str__(self):
        string = self.make + ' ' + self.model
        return string

class Driver(models.Model):
    name = models.CharField(max_length=128)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    main_town = models.CharField(max_length=50)
    main_postal_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Bid(models.Model):
    price = models.CharField(max_length=10)
    comment = models.CharField(max_length=1024)
    ride_request = models.ForeignKey(RideRequest, on_delete=models.CASCADE, default=None)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default=None)

    def __str__(self):
        string = str(self.ride_request) + " " + str(self.price)
        return str(self.ride_request) + " " + str(self.price)


