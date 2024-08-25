from django.contrib import admin
from .models import FuelType, FuelStation, Transaction, Tank, Payment, Attendant

# Register your models with the admin site
admin.site.register(FuelType)
admin.site.register(FuelStation)
admin.site.register(Transaction)
admin.site.register(Tank)
admin.site.register(Payment)
admin.site.register(Attendant)
