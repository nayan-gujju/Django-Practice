from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student
from .forms import StudentForm
# Create your views here.


""" class StudentCreateView(CreateView):
    model = Student
    template_name = 'school/student.html'
    fields = ['name', 'email', 'password']
    success_url = '/thank/'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'namecls'})
        form.fields['email'].widget = forms.TextInput(attrs={'class':'emailcls'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'passcls'})
        return form """

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student.html'
    success_url = '/thank/'


class ThankTemplateView(TemplateView):
    template_name = 'school/thank.html'

class StudentListView(ListView):
    model = Student
    template_name = 'school/student_list.html'
    context_object_name = 'students'