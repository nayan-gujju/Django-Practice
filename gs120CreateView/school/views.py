from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student
# Create your views here.


class StudentCreateView(CreateView):
    model = Student
    template_name = 'school/student.html'
    fields = ['name', 'email', 'password']
    #success_url = '/thank/'

    
class ThankTemplateView(TemplateView):
    template_name = 'school/thank.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/showdata.html'
    context_object_name = 'student'

class StudentListView(ListView):
    model = Student
    template_name = 'school/student_list.html'
    context_object_name = 'students'