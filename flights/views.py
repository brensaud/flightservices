from django.shortcuts import render
from flights.models import Flight, Passenger, Reservation
from flights.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets

# Create your views here.
class FlightViewSet(viewsets.ModelViewset):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

