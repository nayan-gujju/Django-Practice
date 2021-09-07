from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print('i am View')
    return HttpResponse('This is Home View')