from django.urls import path
from . import views
urlpatterns = [
    path('for/', views.learn_for), 
    path('forn/', views.learn_fort)
]