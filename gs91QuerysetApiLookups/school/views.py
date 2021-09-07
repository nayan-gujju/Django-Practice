from django.shortcuts import render
from .models import Student
from datetime import date
# Create your views here.
def home(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(name__iexact='Nayan')
    #student_data = Student.objects.filter(name__exact='Nayan')
    
    #student_data = Student.objects.filter(name__contains='ee')
    #student_data = Student.objects.filter(name__icontains='ee')
    
    #student_data = Student.objects.filter(id__in=[1,5,7,10,3])
    #student_data = Student.objects.filter(marks__in=[45])
    #student_data = Student.objects.filter(marks__gt=45)
    
    #student_data = Student.objects.filter(name__startswith='n')
    #student_data = Student.objects.filter(name__istartswith='n')
   
    #student_data = Student.objects.filter(name__endswith='n')
    #student_data = Student.objects.filter(name__iendswith='n')

    #student_data = Student.objects.filter(passdate__range=('2021-8-1','2021-8-4'))
    
    #student_data = Student.objects.filter(adminssiondate__range=date(2020,3,24))
    #student_data = Student.objects.filter(passdate__year=2021)
    #student_data = Student.objects.filter(passdate__year__gte=2021)
    
    
    """ student_data = Student.objects.filter(passdate__month=8)
    student_data = Student.objects.filter(passdate__day=8)
    student_data = Student.objects.filter(passdate__week=8)
    student_data = Student.objects.filter(passdate__week_day=8) """


    #student_data = Student.objects.filter(passdate__quarter=3)

    student_data = Student.objects.filter(roll__isnull=False)

    print('Returns:', student_data)
    print()
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html', {'students':student_data})