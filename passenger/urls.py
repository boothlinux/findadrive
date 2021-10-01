from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('', PassengerIndex.as_view()),
    path('mydrive/', MyDrive.as_view()),
    path('api/rrlist/', RideRequestList.as_view()),
    path('login/', LoginPage.as_view()),
]