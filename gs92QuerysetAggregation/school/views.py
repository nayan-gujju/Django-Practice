from django.shortcuts import render
from .models import Student
from datetime import date, time
from django.db.models import Avg, Min, Max, Sum, Count

# Create your views here.

def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks')) 
    summ = student_data.aggregate(Sum('marks')) 
    minimum = student_data.aggregate(Min('marks')) 
    maximum = student_data.aggregate(Max('marks')) 
    count = student_data.aggregate(Count('marks')) 


    context = {'students':student_data, 'avg':average, 'sum':summ, 'min':minimum, 'max':maximum, 'count':count}
    
    print("Return:", student_data)
    print()
    print("SQL Query:", student_data.query)
    return render(request, 'school/home.html',context)
