from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    print('This is view ')
    return HttpResponse('This is Home Page')