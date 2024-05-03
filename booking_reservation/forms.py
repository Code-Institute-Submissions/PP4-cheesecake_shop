from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from .models import Booking
from .widget import DatePickerInput, TimePickerInput
from datetime import time


def validate_opening_hours(value):
    opening_time = time(14, 0)
    closing_time = time(23, 0)
    last_booking_time = closing_time.replace(hour=closing_time.hour-1,
                                             minute=0, second=0,
                                             microsecond=0)

    if not (opening_time <= value <= closing_time):
        raise forms.ValidationError("Please select a time within "
                                    "opening hours (2pm - 11pm).")
    elif value > last_booking_time:
        raise forms.ValidationError("Sorry, the last online booking "
                                    "can be made at most 2 hours before "
                                    "closing time.")


class BookingForm(forms.ModelForm):
    reservation_time = forms.TimeField(
        widget=TimePickerInput(attrs={'class': 'form-control'}),
        validators=[validate_opening_hours]
        )

    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'number_of_guests',
                  'reservation_date', 'reservation_time', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name',
                                    'required': True}),
            'email': forms.EmailInput
            (attrs={'placeholder': 'Enter your email'}),
            'phone': forms.TextInput
            (attrs={'placeholder': 'Enter your phone number'}),
            'number_of_guests': forms.NumberInput
            (attrs={'min': 1, 'max': 8}),
            'reservation_date': DatePickerInput
            (attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea
            (attrs={'rows': 2, 'placeholder': 'Enter any special request'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Please enter your name')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Please enter your email address')
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError('Please enter a valid email address')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError('Please enter a valid email address')

        return email

    def clean_number_of_guests(self):
        number_of_guests = self.cleaned_data.get('number_of_guests')
        if number_of_guests is None:
            raise ValidationError('Please enter a valid number of guests')

        if number_of_guests <= 0:
            raise ValidationError('Number of guests must be greater than zero')

        if number_of_guests > 8:
            raise ValidationError('Sorry, we cannot accommodate '
                                  'parties larger than 8 guests')

        return number_of_guests