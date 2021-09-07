from django.shortcuts import render
from django.views.generic.list import ListView 
from .models  import Student
# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'school/student.html'
    context_object_name = 'student'

    def get_queryset(self):
        return Student.objects.filter(course='Django')

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context

    def get_template_names(self):
        if self.request.COOKIES['user'] == 'nayan':
            template_name = 'school/nayan.html'
        else:
            template_name = self.template_name
        return [template_name]