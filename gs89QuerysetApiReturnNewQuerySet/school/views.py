from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
# Create your views here.
def home(request):
    #student_data = Student.objects.all()
    
    #student_data = Student.objects.filter(marks=90)
    
    #only returns exclude this praticular arguments 
    #student_data = Student.objects.exclude(marks=95)
    
    #oreder by this fields 
    #student_data = Student.objects.order_by('city')asending 
    #student_data = Student.objects.order_by('-city')desending 
    #student_data = Student.objects.order_by('?') randomly
    
    #student_data = Student.objects.order_by('id').reverse()[0:4]

    #student_data = Student.objects.values()
    #student_data = Student.objects.values('name','marks')
    
    #student_data = Student.objects.values_list()
    #student_data = Student.objects.values_list('id','name', named=True)
    
    #student_data = Student.objects.using('default')
    
    #student_data = Student.objects.dates('pass_date', 'month')
    
    """ second table 'TEachers 'Started """
    """ qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.union(qs1) """
    
    """ qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.union(qs1, all=True) """

    """ qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.intersection(qs1) """

    """ qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs1.difference(qs2) """
    ############AND OR OPERATOR #############
    
    #student_data = Student.objects.filter(id=2) & Student.objects.filter(roll=170220107114)
    #student_data = Student.objects.filter(id=2, roll=170220107114) 
    #student_data = Student.objects.filter(Q(id=2) & Q(roll=170220107114)) 
    
    student_data = Student.objects.filter(id=22) | Student.objects.filter(roll=170220107114)
    print('Return:', student_data)
    print()
    print('SQL query:', student_data.query)
    return render(request,'school/home.html', {'students': student_data})