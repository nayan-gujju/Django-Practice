from django.urls import path
from signup import views

urlpatterns = [
    path('registration/', views.showdata),
]