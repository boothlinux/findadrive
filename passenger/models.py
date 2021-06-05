from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=128)
    home_town = models.CharField(max_length=50)
    home_postal_code = models.CharField(max_length=7)

    def __str__(self):
        string = self.name
        return string
    
class RideRequest(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, default=None)
    pickup_town = models.ForeignKey('driver.Community', on_delete=models.CASCADE, default=None, blank=True, related_name="pickup_town")
    pickup_street_address = models.CharField(max_length=50)
    pickup_postal_code = models.CharField(max_length=7, blank=True)
    dropoff_town = models.ForeignKey('driver.Community', on_delete=models.CASCADE, default=None, blank=True, related_name="dropoff_town")
    dropoff_street_address = models.CharField(max_length=50)
    dropoff_postal_code = models.CharField(max_length=7, blank=True)
    comments = models.CharField(max_length=1024, blank=True)
    accepted_ride = models.BooleanField(default=False, blank=True)
    rejected_ride_comments = models.CharField(blank=True, max_length=1024)
    completed_ride = models.BooleanField(default=False, blank=True)

    def __str__(self):
        string = str(self.pickup_town) + " to " + str(self.dropoff_town)
        return string


