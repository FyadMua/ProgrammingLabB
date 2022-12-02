from django.contrib import admin
from travelapp.models import Flights,Places,Hotels,City,BookFlight,BookHotel,BookPackage

# Register your models here.
admin.site.register(Flights)
admin.site.register(Places)
admin.site.register(Hotels)
admin.site.register(City)
admin.site.register(BookFlight)
admin.site.register(BookHotel)
admin.site.register(BookPackage)
