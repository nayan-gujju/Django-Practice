from django.shortcuts import render
from .forms import Student
from .models import User
# Create your views here.


def show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pa = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pa)
            reg.save()
            #this is use for update
            #reg = User(id=1, name=nm, email=em, password=pa)
           #reg.save()
           #this is use for delete
            #reg = User(id=1)
            #reg.delete()new = Video()
    else:
        fm = Student()

    return render(request, 'enroll/home.html' , {'form':fm})