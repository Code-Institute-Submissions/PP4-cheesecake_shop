from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path(
        'bookings_list/',
        views.UserBookingsList.as_view(),
        name='bookings_list'
    ),
    path(
        'edit_booking/<int:booking_id>',
        views.EditBookingView.as_view(),
        name='edit_booking'
    ),
    path('delete_booking/<int:booking_id>',
        views.DeleteBookingView.as_view(),
        name='delete_booking'
        ),
    path('confirmation/',
        views.ConfirmationView.as_view(),
        name='confirmation_page'
        ),
]
