from django.urls import path
from . import views
urlpatterns = [
    path('courseone/', views.learn_django)
]