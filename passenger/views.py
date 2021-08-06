from driver.models import Community, Bid
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, ListView
from .models import *
from .forms import RideRequestForm, RegisterForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import json
import simplejson
from django.forms.models import model_to_dict
from .serializers import RideRequestSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



# Create your views here.
class PassengerIndex(CreateView):
    template_name = "passenger/index.html"
    model = RideRequest
    fields = ['pickup_town', 'pickup_street_address', 'dropoff_town', 'dropoff_street_address']
    
    def get_context_data(self, **kwargs):
        context = super(PassengerIndex, self).get_context_data(**kwargs)
        context['communitylist'] = Community.objects.order_by('name_of_community')
        #context['form'] = RideRequestForm()
        return context
    
    def post(self, request):
        form = RideRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.passenger = self.request.user
            instance.save()
            #form.save()
            return redirect('passenger-request')
        else:
            return HttpResponseRedirect('/passenger/')

class RideRequestList(APIView):
    """
    Lists all open RideRequests, or make a new one
    """
    def get(self, request, format=None):
        data = self.get_queryset()
        serializer = RideRequestSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def get_queryset(self):
        return RideRequest.objects.filter(accepted_ride=False, completed_ride=False)

class LoginPage(TemplateView):
    template_name = "passenger/login.html"

    def post(self, request):
        print(request.POST)
        username = request.POST
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/passenger')
        else:
            print("Not logged in!")
            pass

class SignupPage(CreateView):
    template_name = "registration/signup.html"
    form_class = RegisterForm

    def post(self, request):
        form = RegisterForm(self.request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('passenger-home')
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

class CurrentRequest(ListView):
    template_name = "passenger/request.html"
    model = RideRequest


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_ride_request = RideRequest.objects.get(passenger=self.request.user, accepted_ride=False)
        context['pickup_address'] = my_ride_request.pickup_street_address
        context['pickup_town'] = my_ride_request.pickup_town
        context['dropoff_address'] = my_ride_request.dropoff_street_address
        context['dropoff_town'] = my_ride_request.dropoff_town
        try:
            context['bids'] = Bid.objects.filter(ride_request=my_ride_request)
        except:
            context['bids'] = None
        return context