from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from passenger.models import RideRequest
from passenger.forms import RideRequestForm


class DriverIndex(ListView):
    template_name = "driver/index.html"
    model = RideRequest
    #driverequests = RideRequest.objects.filter(accepted_ride=False)

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['riderequestlist'] = RideRequest.objects.all()
        return context
    


