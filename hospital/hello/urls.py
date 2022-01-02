from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Bed
from .views import BloodDonate
from django.urls import path



urlpatterns = [
   

    path("beds.html", views.beds, name="beds"),
    path("bloods.html", views.bloods, name="bloods"),
    
    path("AddBed.html", views.AddBed, name="AddBed"),
    path("AddBlood.html", views.AddBlood, name="AddBlood"),
   
    path('UpdateBed<int:pk>/', views.UpdateBed, name="UpdateBed"),
    path('delete_datam/<int:pk>/', views.delete_datam, name="delete_datam"),
    path('UpdateBlood<int:pk>/', views.UpdateBlood, name="UpdateBlood"),
    path('delete_blood/<int:pk>/', views.delete_blood, name="delete_blood"),
   
 
]
