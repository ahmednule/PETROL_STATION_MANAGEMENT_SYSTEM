from django.db import models
from django.contrib.auth.models import User


class FuelType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FuelStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    fuel_types = models.ManyToManyField(FuelType)
    image = models.ImageField(upload_to='images/',default='images/image1.jpg')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
class Transaction(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Tank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    current_level = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=50)  # e.g., Cash, Credit Card, Mobile Money

class Attendant(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rfid_tag = models.CharField(max_length=50)

    def __str__(self):
        return self.name
