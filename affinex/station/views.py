from django.shortcuts import render,get_object_or_404, redirect
from .models import FuelStation, Transaction, Tank,Payment,Attendant,FuelType
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'station/home.html')
     
def station_detail(request, station_id):
    station = FuelStation.objects.get(id=station_id)
    transactions = Transaction.objects.filter(station=station)
    tanks = Tank.objects.filter(station=station)
    return render(request, 'station/station_detail.html', {'station': station, 'transactions': transactions, 'tanks': tanks})
def stations(request):
    stations = FuelStation.objects.all()
    return render(request, 'station/stations.html', {'stations': stations})


def dashboard(request):
    transaction = Transaction.objects.all()
    tanks = Tank.objects.all()
    return render(request, 'station/dashboard.html', {'sales': transaction, 'tanks': tanks})

def sell_fuel(request, station_id):
    station = get_object_or_404(FuelStation, pk=station_id)
    if request.method == 'POST':
        fuel_type = get_object_or_404(FuelType, pk=request.POST['fuel_type'])
        volume = request.POST['volume']
        amount = request.POST['amount']
        payment_mode = request.POST['payment_mode']
        attendant = get_object_or_404(Attendant, pk=request.POST['attendant'])
        
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
    
    return render(request, 'station/sell_fuel.html', {'station': station})

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'station/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

