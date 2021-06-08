from rest_framework import serializers
from passenger.models import RideRequest

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'