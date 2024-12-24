from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("/register", RegisterUser.as_view()),
    path("/verify/otp", verify_otp),
    path("/resend/otp", resend_otp_to_email),
    path("/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("/token/verify", TokenVerifyView.as_view(), name="token_verify"),
]
