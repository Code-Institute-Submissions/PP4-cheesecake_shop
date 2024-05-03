from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'number_of_guests', 'reservation_date',
                    'reservation_time', 'created_on', 'notes', 'status')
    list_filter = ('reservation_date', 'status',)
    search_fields = ['name', 'number_of_guests', 'reservation_date',
                     'reservation_time']
    actions = ['change_status']

    def change_status(self, request, queryset):
        queryset.update(status='Booked')


# Admin page changes
admin.site.site_header = 'Restaurant Admin Panel'
admin.site.site_title = 'Restaurant App Admin'
admin.site.site_index_title = 'Welcome to Restaurant Admin Panel'