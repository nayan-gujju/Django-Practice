from django.urls import path
from fees import views


urlpatterns = [
    path('feesd/', views.fees_django),
    path('feesp/', views.fees_python)
]