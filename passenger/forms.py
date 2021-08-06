from django.forms import ModelForm
from django import forms
from .models import RideRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=200)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': (
                "Not a valid phone number! Please use like this: 19026641234")})

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2", "email"]

class RideRequestForm(ModelForm):

    class Meta:
        model = RideRequest
        exclude = (
            "accepted_ride",
            "completed_ride",
            "rejected_ride_comments",
        )

