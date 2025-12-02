from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView,
    home,
    register,
    profile,
)

app_name = "blog"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("", home, name="base"),
    path("profile/", profile, name="profile"),
]
