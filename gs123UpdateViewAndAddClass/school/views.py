from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Student
from django import forms
from .forms import StudentForm
# Create your views here.


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student.html'
    context_object_name = 'student'
    """ fields = ('name', 'email', 'password') """
    success_url = '/add/'
    #this class only for create its not for update if you can add this class in update then you can write this function in update view
    """ def form_class(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'namecls'})
        form.fields['password'].widget = forms.TextInput(attrs={'class':'passwordcls'}) """

class StudentListView(ListView):
    model = Student
    template_name = 'school/showdata.html'
    context_object_name = 'students'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm
    """ fields = ('name', 'email', 'password') """
    template_name = 'school/student.html'
    
    
           