from django.shortcuts import render
from flights.models import Flight

from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy


class FlightListView(ListView):
    model = Flight
    template_name = 'flights.html'


class FlightDetailView(DeleteView):
    model = Flight
    template_name = 'flight_detail.html'


class FlightCreateView(CreateView):
    model = Flight
    template_name = 'create_flight.html'
    fields = ['flight_number', 'operating_airlines', 'departure_city', 'arrival_city', 'date_of_departure', 'estimated_time_of_departure',]


class FlightUpdateView(UpdateView):
    model = Flight
    template_name = 'update_flight.html'
    fields = ['departure_city', 'arrival_city', 'date_of_departure', 'estimated_time_of_departure',]


class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
