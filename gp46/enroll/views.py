from django.shortcuts import render
from .forms import StudentInfo
from .models import User
# Create your views here.


def show(request):
    if request.method == 'POST':
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pa = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pa)
            reg =User(name=nm, email=em, password=pa)
            reg.save()
    else:
        fm = StudentInfo()

    return render(request, 'enroll/home.html' , {'form':fm})