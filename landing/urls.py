from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('content/', views.content, name='content'),
]
