from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Home Page')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('<h1> hello Python</h1>')

def learn_var(request):
    a = '<h1> Hello Variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a = 10+10
    return HttpResponse(a)

def learn_format(request):
    a = 'nayan'
    return HttpResponse(f'Name is {a}')