"""hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from service import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login.html', views.login),
    path('logout.html', views.logout),  
    path("appointments.html", views.appointments),
    path("beds.html", views.beds),
    path("nurses.html", views.nurses),
    path("doctors.html", views.doctors),
    path("bloods.html", views.bloods),
    path("organs.html", views.organs),
    path("tests.html", views.tests),
    path("medicines.html", views.medicines),
    path("patients.html", views.patients),
    path("stories.html", views.stories),
    path("AddAppointment.html", views.AddAppointment),
    path("AddBed.html", views.AddBed),
    path("AddDoctor.html", views.AddDoctor),
    path("AddNurse.html", views.AddNurse),
    path("AddOrgan.html", views.AddOrgan),
    path("AddPatient.html", views.AddPatient),
    path("AddStory.html", views.AddStory),
    path("AddNurse.html", views.AddNurse),
    path("AddTest.html", views.AddTest),
    path("AddMedicine.html", views.AddMedicine),
    path("AddBlood.html", views.AddBlood),
  
]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)