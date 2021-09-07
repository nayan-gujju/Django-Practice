from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic.list import ListView
from .models import Student
from .forms import StudentForm
# Create your views here.


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student.html'
    context_object_name = 'student'
    success_url = '/add/'
    

class StudentListView(ListView):
    model = Student
    template_name = 'school/showdata.html'
    context_object_name = 'students'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student.html'
    
    
class DeleteStudentView(DeleteView):
    model = Student
    success_url = '/showdata/'
    
           