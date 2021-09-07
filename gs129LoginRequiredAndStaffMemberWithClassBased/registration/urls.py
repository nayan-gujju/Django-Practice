from django.urls import path 
from registration import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
urlpatterns = [
    path('profile/',login_required(views.ProfileTemplateView.as_view()) , name='profile'),
]