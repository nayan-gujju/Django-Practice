from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Student
# Create your views here.


class StudentCreateView(CreateView):
    model = Student
    template_name = 'school/student.html'
    context_object_name = 'student'
    fields = ('name', 'email', 'password')
    success_url = '/add/'



class StudentListView(ListView):
    model = Student
    template_name = 'school/showdata.html'
    context_object_name = 'students'


class UpdateStudentView(UpdateView):
    model = Student
    fields = ('name', 'email', 'password')
    template_name = 'school/student.html'
    success_url = '/showdata/'
    
           