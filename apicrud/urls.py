from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.flight_list, name="apicrud-list"),
    path('flights/<int:pk>/', views.flight_detail, name="apicrud-detail"),
]