"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('about-us/', views.about_us),
    path('services/', views.services_off, name='services'),
    path('service/<int:id>/', views.service_details, name='service_detail'),
    path('delete/<int:pk>/', views.delete_service, name='delete_service'),
    path('login/', views.login_page),
    path('contact/', views.contact_us),
    path('subscribe/', views.subscribe),
    path('crud/', views.crud, name='crud'),
    path('', include('CRUD.urls'))
]
