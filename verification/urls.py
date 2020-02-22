from django.urls import path, include
from .views import getPhoneNumberRegistered

urlpatterns = [
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
]