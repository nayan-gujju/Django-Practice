from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentInfo 
from enroll.models import User
# Create your views here.

#this is function for add ans show data
def add_show(request):
    if request.method == "POST":
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentInfo()        
    else:
        fm = StudentInfo()      
    stud = User.objects.all()  
    return render(request,'enroll/addandshow.html', {'form':fm, 'stu':stud})


#this function for update

def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentInfo(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentInfo(instance=pi)

    return render(request, 'enroll/update.html', {'form':fm})



#this function for delete

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')