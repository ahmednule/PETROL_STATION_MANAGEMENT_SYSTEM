from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stations/', views.stations, name="stations"),
    path('station/<int:station_id>/', views.station_detail, name='station_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sell_fuel/<int:station_id>/', views.sell_fuel, name='sell_fuel'),
    path('transaction_success/<int:transaction_id>/', views.transaction_success, name='transaction_success'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
