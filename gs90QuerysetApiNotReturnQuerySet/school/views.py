from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
# Create your views here.
def home(request):
    
    student_data = Student.objects.get(pk=1)
    
    #student_data = Student.objects.first()
    #student_data = Student.objects.order_by('name').first()
    
    #student_data = Student.objects.last()
    
    #student_data = Student.objects.latest('pass_date')
    
    #student_data = Student.objects.earliest('pass_date')
    
    """  student_data = Student.objects.all()
    print(student_data.exists()) """

    #student_data = Student.objects.create(name='jaydeep', roll=106, city='Patan', marks=89, pass_date='2010-3-24')
    
    """ student_data, created = Student.objects.get_or_create(name='jaydeep', roll=106, city='Patan', marks=89, pass_date='2010-3-24')
    print('Created:', created) """
    
    #student_data = Student.objects.filter(id=5).update(roll=170220107105) 
    
    """ student_data, created = Student.objects.update_or_create(id=5, name='jaydep', defaults={'name':'kaival'})
    print('Created:', created) """

    """ objs = [
        Student(name='sagar', roll=170220107009, city='amreli', marks=32, pass_date='2021-6-18'),
        Student(name='harshil', roll=170220107002, city='amreli', marks=82, pass_date='2021-6-20'),
        Student(name='ved', roll=170220107021, city='mhesana', marks=52, pass_date='2021-6-19'),
    ]

    student_data = Student.objects.bulk_create(objs) """

    """ all_student_data = Student.objects.all()
    for stu in all_student_data:
        stu.city = 'Patan'
    student_data = Student.objects.bulk_update(all_student_data, ['city']) """


    #student_data = Student.objects.in_bulk([1,2])
    #student_data = Student.objects.in_bulk([])
    #student_data = Student.objects.in_bulk()
    #print(student_data[2].name)

    """ student_data = Student.objects.get(pk=5)
    deleted = student_data.delete()
    #Delete in bulk
    student_data = Student.objects.filter(marks=90).delete()
    #Delete All Records
    student_data = Student.objects.all().delete() """

    """ student_data = Student.objects.all()
    print (student_data.count()) """

    
    print('Return:', student_data)
    print()
    
    return render(request,'school/home.html', {'student': student_data})