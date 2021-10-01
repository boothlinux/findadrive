from django.urls import path
from django.views.generic import TemplateView, ListView
from .views import *


urlpatterns = [
    path('mydrive/', MyDrive.as_view()),
    path('', PassengerIndex.as_view(), name='passenger-home'),
    path('api/rrlist/', RideRequestList.as_view()),
    path('login/', LoginPage.as_view(), name='passenger-login'),
    path('signup', SignupPage.as_view(), name='passenger-signup'),
    path('request', CurrentRequest.as_view(), name='passenger-request'),
]