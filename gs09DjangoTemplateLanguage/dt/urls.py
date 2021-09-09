from django.urls import path
from . import views

urlpatterns = [
    path('dati/', views.date_time)
]