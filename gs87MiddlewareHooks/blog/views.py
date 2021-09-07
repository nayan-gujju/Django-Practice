from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse 
# Create your views here.
def home(request):
    print('i am Home View')
    return HttpResponse('This is Home View')

def excp(request):
    print('i am Exception View')
    a = 10/0
    return HttpResponse('This is Excp View')

def user_info(request):
    print('i am User info View')
    context = {'name': 'Nayan'}
    return TemplateResponse(request,'blog/user.html', context)