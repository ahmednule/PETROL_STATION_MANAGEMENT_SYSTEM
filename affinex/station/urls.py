from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

urlpatterns = [
    path('station/', views.home_view, name='home'),
    path('', views.station, name="stations"),
    path('station/<int:station_id>/', views.station_detail, name='station_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sell_fuel/', views.sell_fuel, name='sell_fuel'),
    path('transaction_success/<int:transaction_id>/', views.transaction_success, name='transaction_success'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
