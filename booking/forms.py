from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """Custom widget that specifically handles dates"""
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """Form to book a table"""
    class Meta:
        """Meta class"""
        model = Booking
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'date_of_booking': DateInput(),
            'notes': forms.Textarea(attrs={
                'rows': 4,
                'cols': 30,
                'placeholder': 'Allergies and other notes...'})
            }