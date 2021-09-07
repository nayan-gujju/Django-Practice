from django.shortcuts import render
from .forms import StudentInfo
# Create your views here.

def showformdata(request):
    fm = StudentInfo()
    
    return render(request, 'enroll/userregistration.html', {'form':fm})