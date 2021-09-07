from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def results_django(request):
    return HttpResponse('results-->results_django')

def results_python(request):
    return HttpResponse('results-->results_python')