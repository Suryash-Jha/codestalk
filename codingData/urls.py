from django.urls import path, include
from . import views

urlpatterns = [
    path("user/<str:id>", views.getBasicData, name="codingData"),
    path("", views.index, name="index"),
]
