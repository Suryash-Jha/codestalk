from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginx, name="login"),
    path("logout/", views.logoutx, name="logout"),

]
