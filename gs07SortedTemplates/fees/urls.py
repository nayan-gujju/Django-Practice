from django.urls import path
from fees import views


urlpatterns = [
    path('feesdjango/', views.fees_django),
    path('feespython/', views.fees_python)
]