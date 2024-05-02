from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
#def home_view(request):
#   return render(request,'booking/index.html')
    
class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    def get(self, request):
        return render(request, 'index.html')


class Menu(generic.DetailView):
    """
    Renders the Menu page in the browser
    """
    def get(self, request):
        return render(request, 'menu.html')


class BookingView(CreateView):
    # model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    # success_message = "Booking successful!"

    def booking_view(self, request):
        return render(request, 'booking.html')

    def post(self, request):
        form = BookingForm(data=request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.author = request.user
            booking.save()

            return redirect('confirmation_page')  # Red. to confirmation page
        else:
            messages.error(request, "Invalid booking. Please ensure \
            your booking date is not in the past \
            and that a unique nickname is used.")
        return redirect('booking')  # Red. to the booking page with errors


class UserBookingsList(View):
    """
        Directs to the user's booking page, and retrieves 
        all reservations made by the user.
    """

    def get(self, request,):
        bookings = Booking.objects.filter(author=request.user)
        all_res = Booking.objects.all()
        context = {
            'bookings': bookings,
            'all_res': all_res
        }
        return render(request, 'bookings_list.html', context)


class EditBookingView(View):
    """
        Allows the user to edit a reservation.
    """

    def get(self, request, booking_id):
        booking = get_object_or_404(
            Booking,
            id=booking_id,
            author=request.user
        )
        form = BookingForm(instance=booking)
        context = {
            'form': form,
            'booking': booking,
        }
        return render(request, 'edit_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(
            Booking,
            id=booking_id,
            author=request.user
        )
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')  # Red. to bookings list
        else:
            messages.error(request, "Invalid booking. \
            Please ensure your booking date is not in the past.")
        context = {
            'form': form,
            'booking': booking,
        }
        return render(request, 'edit_booking.html', context)


class DeleteBookingView(View):
    """
    Allows the user to delete a reservation.
    """

    def get(self, request, booking_id):
        booking = get_object_or_404(
            Booking,
            id=bookingn_id,
            author=request.user
        )
        return render(
            request,'delete_booking.html',
            {'reservation': booking}
        )

    def post(self, request, booking_id):
        booking = get_object_or_404(
            Booking,
            id=booking_id,
            author=request.user
        )
        reservation.delete()
        return redirect('bookings_list')  # Red. to the reservations list


class ConfirmationView(View):
    """
    View for handling the confirmation page
    after a successful booking.
    """
    template_name = 'booking_confirmation.html'

    def get(self, request):
        return render(request, 'booking_confirmation.html')
