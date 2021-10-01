from driver.models import Community, Bid
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, ListView
from passenger.models import *
from passenger.forms import RideRequestForm, RegisterForm
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
from passenger.serializers import RideRequestSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class MainPage(TemplateView):
    template_name = "index.html"

    def post(self, request):
        print(request.POST)
        if request.POST == "Hi":
            print("hi")
        if request.user is not None:
            return HttpResponseRedirect('/passenger')
        else:
            print("Not logged in!")
            pass