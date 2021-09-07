from django.shortcuts import render
from .forms import StudentInfo
from django.contrib import messages
# Create your views here.

def showdata(request):
    messages.info(request, 'Now you can login...')
    messages.success(request, 'update...')
    messages.warning(request, 'this is warning ...')
    messages.error(request, 'this is error.')
    fm = StudentInfo()

    return render(request, 'enroll/userregistration.html' , {'form':fm})