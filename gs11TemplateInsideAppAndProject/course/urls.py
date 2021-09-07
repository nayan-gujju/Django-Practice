from django.urls import path
from . import views
urlpatterns = [
    path('courselearn/', views.learn_course),
]