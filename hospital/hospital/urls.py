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
    path("AddOrgan.html", views.AddOrgan),
    path("users.html", views.users),
    path("AddUser.html", views.AddUser),
    path('UpdateOrgan<int:pk>/', views.UpdateOrgan),
    path('delete_organ/<int:pk>/', views.delete_organ),
    path('UpdateUser<int:pk>/', views.UpdateUser),
    path('delete_user/<int:pk>/', views.delete_user),
    path('hello/', include('hello.urls')),

]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

