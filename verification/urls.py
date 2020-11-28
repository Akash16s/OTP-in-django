from django.urls import path, include
from .views import getPhoneNumberRegistered, getPhoneNumberRegistered_TimeBased

urlpatterns = [
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
]