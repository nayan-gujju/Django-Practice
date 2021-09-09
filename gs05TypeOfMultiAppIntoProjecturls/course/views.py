from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course_django(request):
    return HttpResponse('course-->Course_django')

def course_python(request):
    return HttpResponse('course-->Course_python')
    
