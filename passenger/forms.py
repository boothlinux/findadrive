from django.forms import ModelForm
from .models import RideRequest

class RideRequestForm(ModelForm):

    class Meta:
        model = RideRequest
        exclude = (
            "accepted_ride",
            "completed_ride",
            "rejected_ride_comments",
        )

