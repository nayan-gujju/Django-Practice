from django.urls import path
from course import views

urlpatterns = [
    path('learnd/', views.learn_django), 
    path('learnp/', views.learn_python),
]