from django.urls import path
from .views import reservation_booking, booking_confirmation

urlpatterns = [    
    path('reservation_booking/',
         reservation_booking,
         name='reservation_booking'),
    path('booking_confirmation/',
         booking_confirmation,
         name='booking_confirmation'),
]