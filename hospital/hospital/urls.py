"""hospital URL Configuration

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
from hello import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("nurses.html", views.nurses),
    path("medicines.html", views.medicines),
    path("AddNurse.html", views.AddNurse),
    path("AddNurse.html", views.AddNurse),
    path("AddMedicine.html", views.AddMedicine),
    path('UpdateMedicine<int:pk>/', views.UpdateMedicine),
    path('delete_medicine/<int:pk>/', views.delete_medicine),
    path('UpdateNurse<int:pk>/', views.UpdateNurse),
    path('delete_nurse/<int:pk>/', views.delete_nurse),
    path('hello/', include('hello.urls')),

]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

