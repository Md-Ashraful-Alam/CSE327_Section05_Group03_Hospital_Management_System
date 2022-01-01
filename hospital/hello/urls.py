from django.contrib import admin
from django.urls import path, include
from .import views
from .views import Patient
from .views import Story
from django.urls import path
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
   
    
    path("patients.html", views.patients, name="patients"),
    path("stories.html", views.stories, name="stories"),
    path("AddPatient.html", views.AddPatient, name="AddPatient"),
    path("AddStory.html", views.AddStory, name="AddStory"),
    path('UpdatePatient<int:pk>/', views.UpdatePatient, name="UpdatePatient"),
    path('delete_patient/<int:pk>/', views.delete_patient, name="delete_patient"),
    path('UpdateStory<int:pk>/', views.UpdateStory, name="UpdateStory"),
    path('delete_story/<int:pk>/', views.delete_story, name="delete_story"),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
