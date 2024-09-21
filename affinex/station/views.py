from django.shortcuts import render,get_object_or_404, redirect
from .models import FuelStation, Transaction, Tank,Payment,Attendant,FuelType,UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm,SaleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .models import UserProfile, User

def home_view(request):
    stations = FuelStation.objects.all()
    return render(request, 'station/stations.html')
def station(request):
    stations = FuelStation.objects.all()
    return render(request, 'station/stations.html', {'stations': stations})


@login_required     
def station_detail(request, station_id):
    station = FuelStation.objects.get(id=station_id)
    transactions = Transaction.objects.filter(station=station)
    tanks = Tank.objects.filter(station=station)
    return render(request, 'station/station_detail.html', {'station': station, 'transactions': transactions, 'tanks': tanks})
# @login_required 
def home(request):
    stations = FuelStation.objects.all()
    return render(request, 'station/stations.html', {'stations': stations})

@login_required 
def dashboard(request):
    transaction = Transaction.objects.all()
    tanks = Tank.objects.all()
    return render(request, 'station/dashboard.html', {'sales': transaction, 'tanks': tanks})
@login_required 
def sell_fuel(request):
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    # Get the user's station
    user_profile = get_object_or_404(UserProfile, user=request.user)
    station = user_profile.station

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            fuel_type = form.cleaned_data['fuel_type']
            volume = form.cleaned_data['volume']
            amount = form.cleaned_data['amount']
            payment_mode = form.cleaned_data['payment_mode']
            attendant = get_object_or_404(Attendant, pk=form.cleaned_data['attendant'])

            # Create the transaction
            transaction = Transaction.objects.create(
                station=station,
                fuel_type=fuel_type,
                volume=volume,
                amount=amount
            )

            # Create the payment
            Payment.objects.create(
                transaction=transaction,
                payment_mode=payment_mode
            )

            # Redirect or show a success message
            return redirect('transaction_success', transaction_id=transaction.id)
    else:
        form = SaleForm()

    return render(request, 'station/sell_fuel.html', {'form': form, 'station': station})
@login_required 
def transaction_success(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, 'station/transaction_success.html', {'transaction': transaction})
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'station/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('stations')
#         else:
#             print(form.errors)  # This will print out why the form is invalid
#     else:
#         form = AuthenticationForm()
#     return render(request, 'station/login.html', {'form': form})

def login_view(request):
    return render(request,"station/login.html")

def LoginUser(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        password=request.POST["password"]
##checking username with database
        user=User.objects.get(Username=uname)
        if user.Password==password:
            request.session["Username"]=user.Username
            request.session["Email"]=user.Email
            return render(request,"apps/properties.html")
        else:
            message="Password does not match"
            return render(request,"apps/login.html",{'msg':message})
    else:
        message="User does not exists"
        return render(request,"apps/register.html",{'msg':message})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

