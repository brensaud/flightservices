from django.db import models
from django.urls import reverse


# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure=models.TimeField()

    def get_absolute_url(self):
        return reverse('flight_detail', args=[str(self.id)])

    def __str__(self):
        return self.flight_number


class Passenger(models.Model):
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d/", null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name


class Reservation(models.Model):
    # A flight can be a part of multiple reservations
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight.flight_number } {self.passenger.first_name}' 
