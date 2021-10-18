from django.urls import path
from .views import RegisterView, LogoutAPIView, SetNewPasswordAPIView, LoginAPIView, ResetPasswordAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/', ResetPasswordAPIView.as_view(),
         name="reset-password"),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
]