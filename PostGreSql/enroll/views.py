from django.shortcuts import render
from .forms import Student
from .models import Student_Info 
# Create your views here.

def show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pa = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pa)
            reg = Student_Info(name=nm, email=em, password=pa)
            reg.save()
    else:
        fm = Student_Info()

    return render(request, 'enroll/home.html' , {'form':fm})