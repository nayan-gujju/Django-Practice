from django.shortcuts import render
from .forms import StudentInfo
# Create your views here.

def showformdata(request):
    fm = StudentInfo(auto_id=False, label_suffix=' -', initial={'name':'Meet'})
    return render(request, 'enroll/userregistration.html', {'form':fm})