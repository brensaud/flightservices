from django.urls import path
from .views import (
    FlightListView,
    FlightDetailView,
    FlightCreateView,
    FlightUpdateView,
    FlightDeleteView,
)
urlpatterns = [
    path('', FlightListView.as_view(), name = 'home'),
    path('flight/<int:pk>/', FlightDetailView.as_view(), name = 'flight_detail'),
]