from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FuelStation,Payment,FuelType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CustomUserCreationForm(UserCreationForm):
    station = forms.ModelChoiceField(
        queryset=FuelStation.objects.all(),
        required=True,
        help_text="Select your petrol station."
    )

    class Meta:
        model = User  # Use Django's built-in User model
        fields = ['username', 'email', 'station', 'password1', 'password2']

class SaleForm(forms.Form):
    station = forms.ModelChoiceField(
        queryset=FuelStation.objects.all(),
        required=True,
        help_text="Select the petrol station."
    )
    fuel_type = forms.ModelChoiceField(
        queryset=FuelType.objects.all(),
        required=True,
        help_text="Select the type of fuel."
    )
    volume = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        help_text="Enter the volume of fuel sold."
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        help_text="Enter the amount of sale."
    )
    payment_mode = forms.ChoiceField(
        choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Mobile Money', 'Mobile Money')],
        required=True,
        help_text="Select the mode of payment."
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
