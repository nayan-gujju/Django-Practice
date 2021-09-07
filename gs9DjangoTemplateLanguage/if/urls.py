from django.urls import path
from . import views
urlpatterns = [
    path('if/', views.learn_if),
]