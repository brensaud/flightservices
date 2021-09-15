from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_lenght=10)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure=models.TimeField()


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)



    

