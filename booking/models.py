from datetime import datetime, time
import pytz

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.

class Booking(models.Model):
    DUBLIN_TZ = pytz.timezone('Europe/Dublin')

    TIME_SLOTS = (
        (0, DUBLIN_TZ.localize(datetime.strptime('12:30', '%H:%M')).time()),
        (1, DUBLIN_TZ.localize(datetime.strptime('13:00', '%H:%M')).time()),
        (2, DUBLIN_TZ.localize(datetime.strptime('13:30', '%H:%M')).time()),
        (3, DUBLIN_TZ.localize(datetime.strptime('14:00', '%H:%M')).time()),
        (4, DUBLIN_TZ.localize(datetime.strptime('14:30', '%H:%M')).time()),
        (5, DUBLIN_TZ.localize(datetime.strptime('15:00', '%H:%M')).time()),
        (6, DUBLIN_TZ.localize(datetime.strptime('15:30', '%H:%M')).time()),
        (7, DUBLIN_TZ.localize(datetime.strptime('16:00', '%H:%M')).time()),
        (8, DUBLIN_TZ.localize(datetime.strptime('16:30', '%H:%M')).time()),
    )

    NUM_OF_GUESTS_SELECTION = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking"
    )
    num_of_guests = models.CharField(
        choices=NUM_OF_GUESTS_SELECTION,
        max_length=2
    )
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    update_on = models.DateTimeField(auto_now=True)
    date_of_booking = models.DateField(default=timezone.now)
    time_of_booking = models.IntegerField(choices=TIME_SLOTS, default=0)
    notes = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=100)
    nick_name = models.CharField(
            max_length=50,
            unique=True,
            blank=True,
            null=True
    )

    def clean(self):
        """
        Validation to check if the date_of_booking is in the future
        and if the time_of_booking is in the past for the current date.
        """
        now = timezone.now()

        if self.date_of_booking < now.date():
            raise ValidationError(
                {'date_of_booking':
                    "It looks like you've selected a date in the past. \
                    Please choose a date in the future to proceed with booking."},
                code='invalid_date'
            )

        selected_time = self.TIME_SLOTS[self.time_of_booking][1]

        selected_datetime = self.DUBLIN_TZ.localize(
            datetime.combine(self.date_of_booking, selected_time)
        )

        if self.date_of_booking == now.date() and selected_datetime < now:
            raise ValidationError(
                {'time_of_booking':
                    "It looks like you've selected a time in the past for \
                    today. Please choose a future time for your booking."},
                code='invalid_time'
            )

    def get_time_display(self):
        """
        Get the display value for the time_of_booking field.
        """
        return self.TIME_SLOTS[self.time_of_booking][1].strftime('%H:%M')

    class Meta:
        """Meta class for Reservation model"""
        ordering = ['created_on']

    def __str__(self):
        return f"Booking made by {self.full_name}"