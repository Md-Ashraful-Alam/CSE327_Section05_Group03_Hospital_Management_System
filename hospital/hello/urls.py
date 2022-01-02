from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Nurse
from .views import Medicine
from django.urls import path



urlpatterns = [
   
    path("nurses.html", views.nurses, name="nurses"),
    path("medicines.html", views.medicines, name="medicines"),
    path("AddMedicine.html", views.AddMedicine, name="AddMedicine"),
    path("AddNurse.html", views.AddNurse, name="AddNurse"),
    path("AddNurse.html", views.AddNurse, name="AddNurse"),
    path('UpdateMedicine<int:pk>/', views.UpdateMedicine, name="UpdateMedicine"),
    path('delete_medicine/<int:pk>/', views.delete_medicine, name="delete_medicine"),
    path('UpdateNurse<int:pk>/', views.UpdateNurse, name="UpdateNurse"),
    path('delete_nurse/<int:pk>/', views.delete_nurse, name="delete_nurse"),
    
 
]
