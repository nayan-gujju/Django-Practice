from django.shortcuts import render
from .forms import Student, Teacher
# Create your views here.


def student_from(request):
    if request.method == "POST":
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = Student(request.POST)

    return render(request, 'enroll/student.html' , {'form':fm})

def teacher_from(request):
    if request.method == "POST":
        fm = Teacher(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = Teacher(request.POST)

    return render(request, 'enroll/teacher.html' , {'form':fm})