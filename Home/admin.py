from django.contrib import admin
from .models import Departments,Doctorss,Booking,Contact

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctorss)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_email','content') 
admin.site.register(Contact)             
