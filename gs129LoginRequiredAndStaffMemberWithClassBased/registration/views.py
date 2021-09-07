from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'


class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

