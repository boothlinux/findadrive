from django.db import models
from passenger.models import RideRequest
from django.contrib.auth.models import User


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
    driver = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return str(self.ride_request.passenger) + " - " + str(self.ride_request.pickup_town) + " to " + str(self.ride_request.dropoff_town)


