from django.shortcuts import render
from .models import Student, ExamCenter
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    exam_data = ExamCenter.objects.all()
    
    return render(request, 'school/home.html',{'students':student_data, 'exam':exam_data})