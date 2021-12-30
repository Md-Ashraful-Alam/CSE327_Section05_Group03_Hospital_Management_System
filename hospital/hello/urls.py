from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Patient
from .views import Story
from django.urls import path



urlpatterns = [
   
    
    path("patients.html", views.patients, name="patients"),
    path("stories.html", views.stories, name="stories"),
    path("AddPatient.html", views.AddPatient, name="AddPatient"),
    path("AddStory.html", views.AddStory, name="AddStory"),
    path('UpdatePatient<int:pk>/', views.UpdatePatient, name="UpdatePatient"),
    path('delete_patient/<int:pk>/', views.delete_patient, name="delete_patient"),
    path('UpdateStory<int:pk>/', views.UpdateStory, name="UpdateStory"),
    path('delete_story/<int:pk>/', views.delete_story, name="delete_story"),

]
