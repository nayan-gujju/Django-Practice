from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.showmoredata),
    path('success/', views.thankyou),
]