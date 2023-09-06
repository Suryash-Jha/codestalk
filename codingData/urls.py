from django.urls import path, include
from . import views

urlpatterns = [
    path("user/<str:id>", views.retrieveFromDb, name="codingData"),
    path("", views.index, name="index"),
    path("createId/", views.createId, name="createId"),
    path("api/<str:id>", views.apiRes, name="api"),
    path("users/", views.getAllUsers, name="allUser"),
    
    
]
