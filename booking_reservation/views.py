from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Booking
from .forms import BookingForm

# Create your views here.

@login_required
def reservation_booking(request):
    booking_form = BookingForm()

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking is being reviewed.')
            return redirect('booking_confirmation')

    context = {'form': booking_form}
    return render(request, 'booking_form.html', context)


def booking_confirmation(request):
    booking = Booking.objects.first()
    context = {'booking': booking}
    return render(request,'booking_confirmation.html', context)