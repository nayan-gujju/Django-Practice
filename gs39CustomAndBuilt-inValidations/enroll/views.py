from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.forms import StudentInfo
# Create your views here.



    


def showmoredata(request):
    if request.method == 'POST':
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            print('form validated')
            name = fm.cleaned_data['name']
            print('Name: ', name)
           
            print("Email:", fm.cleaned_data['email'])
    else:
        fm = StudentInfo()
    return render(request, 'enroll/home.html', {'form':fm})