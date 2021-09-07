from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_django(request):
    return HttpResponse('fees-->fees_django')

def fees_python(request):
    return HttpResponse('fees-->fees_python')