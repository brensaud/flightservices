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
    path('flight/<int:pk>/delete', FlightDeleteView.as_view(), name='delete_flight'),
    path('flight/<int:pk>/', FlightDetailView.as_view(), name = 'flight_detail'),
    path('flight/<int:pk>/edit/', FlightUpdateView.as_view(), name = 'flight_edit'),
    path('flight/new/', FlightCreateView.as_view(), name = 'create_flight'),
]