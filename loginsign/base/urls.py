from django.urls import path, include
from .views import authView, home

urlpatterns = [
    path("", home, name="home.html"),
    path("signup/", authView, name="signup.html"),
    path("accounts/", include("django.contrib.auth.urls")),

]
