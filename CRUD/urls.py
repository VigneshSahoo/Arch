from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.create),
    path('update/', views.update),
    path('delete/', views.delete),
    path('read/', views.read),
]
