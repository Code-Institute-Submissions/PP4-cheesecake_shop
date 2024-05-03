from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
import datetime


# Create your models here.
STATUS = (('Pending', 'Pending'), ('Booked', 'Booked'))


# Model for Booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=30, null=False, blank=True)
    number_of_guests = models.IntegerField(default=2)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    reservation_date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)])
    reservation_time = models.TimeField(default=timezone.now)
    notes = models.TextField(max_length=300, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default='Pending')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def __str__(self):
        return (f"Reservation for {self.name} on {self.reservation_date} "
                f"at {self.reservation_time}")