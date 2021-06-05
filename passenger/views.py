from driver.models import Community
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from .models import *
from .forms import RideRequestForm
from django.http import HttpResponseRedirect


# Create your views here.
class PassengerIndex(CreateView):
    template_name = "passenger/index.html"
    model = RideRequest
    form = RideRequestForm
    fields = ['passenger', 'pickup_town', 'pickup_street_address', 'dropoff_town', 'dropoff_street_address']
    
    def get_context_data(self, **kwargs):
        context = super(PassengerIndex, self).get_context_data(**kwargs)
        context['communitylist'] = Community.objects.order_by('name_of_community')
        #context['form'] = RideRequestForm()
        return context
    
    def post(self, request):
        form = RideRequestForm(request.POST)
            
        if form.is_valid():
            print("")
            form.save()
            return HttpResponseRedirect('/passenger/')
        else:
            return HttpResponseRedirect('/passenger/')