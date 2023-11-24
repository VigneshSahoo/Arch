from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.create),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('delete/', views.delete_css),
    path('read/', views.read, name='read'),
]
