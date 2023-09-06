from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginx, name="login"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginx, name="login"),
]
