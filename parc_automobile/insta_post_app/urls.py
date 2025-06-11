from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter)
]