from django.contrib import admin
from django.urls import path, include
from .import views
from .views import User

from .views import OrganDonate

from django.urls import path



urlpatterns = [
   
    path("users.html", views.users, name="users"),
    path("AddUser.html", views.AddUser, name="AddUser"),
    path("AddOrgan.html", views.AddOrgan, name="AddOrgan"),
    path('UpdateOrgan<int:pk>/', views.UpdateOrgan, name="UpdateOrgan"),
    path('delete_organ/<int:pk>/', views.delete_organ, name="delete_organ"),
    path('UpdateUser<int:pk>/', views.UpdateUser, name="UpdateUser"),
    path('delete_user/<int:pk>/', views.delete_user, name="delete_user"),
 
]
