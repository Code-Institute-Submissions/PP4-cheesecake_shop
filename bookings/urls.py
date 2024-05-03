from django.urls import path
from bookings.views import booking_list, booking_edit, booking_delete


urlpatterns = [
    path('booking_list/', booking_list, name='booking_list'),
    path('booking_list/<int:pk>/edit/', booking_edit, name='booking_edit'),
    path('booking_list/<int:pk>/delete/',
         booking_delete, name='booking_delete'),
]