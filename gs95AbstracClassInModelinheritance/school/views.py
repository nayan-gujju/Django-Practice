from django.shortcuts import render
from .models import Student, Teacher, Construction
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    construction_data = Construction.objects.all()
    return render(request, 'school/home.html',{'students':student_data, 'teachers':teacher_data, 'conns':construction_data})