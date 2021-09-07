from django.urls import path
from . import views
urlpatterns = [
    path('feeslearn/', views.fees_learn),
]