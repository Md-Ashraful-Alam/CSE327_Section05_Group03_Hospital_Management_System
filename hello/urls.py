from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Appointment
from .views import Doctor
from .views import Test
from django.urls import path



urlpatterns = [
   
    path("login.html", views.login, name="login"),
    path("logout.html", views.logout, name="logout"),
    path("register.html", views.register, name="register"),
   # path('api/register/', RegisterAPI.as_view(), name='register'),
    path("appointments.html", views.appointments, name="appointments"),
    
    path("doctors.html", views.doctors, name="doctors"),
    path("tests.html", views.tests, name="tests"),
    path("AddAppointment.html", views.AddAppointment, name="AddAppointment"),
    path("AddDoctor.html", views.AddDoctor, name="AddDoctor"),
    
    path("AddTest.html", views.AddTest, name="AddTest"),
   
    path('UpdateAppointment<str:pk>', views.UpdateAppointment, name='UpdateAppointment'),
    path('delete_datas/<str:pk>/', views.delete_datas, name="delete_datas"),
   
    path('UpdateDoctor<int:pk>/', views.UpdateDoctor, name="UpdateDoctor"),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name="deletedoctor"),
    
    path('UpdateTest<int:pk>/', views.UpdateTest, name="UpdateTest"),
    path('delete_test/<int:pk>/', views.delete_test, name="delete_test"),
 
]
