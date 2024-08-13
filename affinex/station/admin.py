from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FuelType, FuelStation, Transaction, Tank, Payment, Attendant, CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    model = CustomUser
    add_form = CustomUserCreationForm

    # Customize the fields displayed in the admin interface
    list_display = ['username', 'station', 'is_staff', 'is_active']
    search_fields = ['username', 'station__name']  # Adjust search fields as needed
    ordering = ['username']

    # Define the fields and fieldsets in the user creation and change forms
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('station',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'station', 'password1', 'password2'),
        }),
    )

# Register your models with the admin site
admin.site.register(FuelType)
admin.site.register(FuelStation)
admin.site.register(Transaction)
admin.site.register(Tank)
admin.site.register(Payment)
admin.site.register(Attendant)
admin.site.register(CustomUser, CustomUserAdmin)
