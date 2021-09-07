from django.urls import path

from . import views

urlpatterns = [
    path('learndjango/', views.learn_django, name="djangoo"),
]