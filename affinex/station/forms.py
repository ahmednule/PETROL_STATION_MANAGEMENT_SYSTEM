from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, FuelStation

class CustomUserCreationForm(UserCreationForm):
    station = forms.ModelChoiceField(
        queryset=FuelStation.objects.all(),
        required=True,
        help_text="Select your petrol station."
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'station', 'password1', 'password2']
