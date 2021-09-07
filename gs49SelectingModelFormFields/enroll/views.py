from django.shortcuts import render
from .forms import Student
# Create your views here.

def showdata(request):
    fm = Student()
    return render(request, 'enroll/home.html', {'form':fm})