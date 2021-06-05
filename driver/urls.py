from django.urls import path
from django.views.generic import TemplateView
from driver.views import DriverIndex


urlpatterns = [
    path('dashboard', DriverIndex.as_view()),
]