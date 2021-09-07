from django.urls import path
from course import views

urlpatterns = [
    path('coursed/', views.course_django), 
    path('coursep/', views.course_python),
]