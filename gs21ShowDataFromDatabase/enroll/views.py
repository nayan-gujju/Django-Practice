from django.shortcuts import render
from enroll.models import Student
# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()#get all data
    #stud = Student.objects.get(pk=2)#get only 
    print('MyOutput:', stud)
    return render(request, 'enroll/studetails.html', {'std':stud})  