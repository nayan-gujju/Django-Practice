from django.shortcuts import render
from .forms import StudentInfo
from django.contrib import messages
# Create your views here.

def showdata(request):
    if request.method == 'POST':
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            fm.save()
            #messages.add_message(request, messages.SUCCESS, 'Your account has been created!!....')
            messages.info(request, 'Your account has been created!!.....')
            print(messages.get_level(request))
            messages.debug(request, 'This is debug.......')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is new debug.......')
            print(messages.get_level(request))
    else:
        fm = StudentInfo()

    return render(request, 'enroll/userregistration.html' , {'form':fm})