from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Appointment
from .views import Bed
from .views import BloodDonate
from .views import Doctor
from .views import Patient
from .views import Nurse
from .views import OrganDonate
from .views import Medicine
from .views import Story
from .views import Test


urlpatterns = [
   
    path("login.html", views.login, name="login"),
    path("logout.html", views.logout, name="logout"),
    path("register.html", views.register, name="register"),
    path("appointements.html", views.appointements, name="appointements"),
    path("beds.html", views.beds, name="beds"),
    path("nurses.html", views.nurses, name="nurses"),
    path("doctors.html", views.doctors, name="doctors"),
    path("bloods.html", views.bloods, name="bloods"),
    path("organs.html", views.organs, name="organs"),
    path("tests.html", views.tests, name="tests"),
    path("medicines.html", views.medicines, name="medicines"),
    path("patients.html", views.patients, name="patients"),
    path("stories.html", views.stories, name="stories"),
    path("AddAppointment.html", views.AddAppointment, name="AddAppointment"),
    path("AddBed.html", views.AddBed, name="AddBed"),
    path("AddDoctor.html", views.AddDoctor, name="AddDoctor"),
    path("AddMedicine.html", views.AddMedicine, name="AddMedicine"),
    path("AddNurse.html", views.AddNurse, name="AddNurse"),
    path("AddOrgan.html", views.AddOrgan, name="AddOrgan"),
    path("AddPatient.html", views.AddPatient, name="AddPatient"),
    path("AddStory.html", views.AddStory, name="AddStory"),
    path("AddNurse.html", views.AddNurse, name="AddNurse"),
    path("AddTest.html", views.AddTest, name="AddTest"),
    path("AddBlood.html", views.AddBlood, name="AddBlood"),


]
