from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    RegisterCreateView,
    RegisterDoneView,
    DonateView,
    # DonationUserDetailView,
    payment_process,
    anonym_payment_process,
)

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register"),
    path("congratulation/", RegisterDoneView.as_view(), name="register_done"),
    path("donate/", DonateView.as_view(), name='donate'),
    path('profile/<str:membership_id>56443323454555/', payment_process, name='profile'),
    path('pay-anonym/',  anonym_payment_process, name='anonym'),
]

