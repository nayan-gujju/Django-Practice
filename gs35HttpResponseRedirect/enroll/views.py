from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.forms import StudentInfo
# Create your views here.

def thankyou(request):
    return render(request, 'enroll/success.html')




def showmoredata(request):
    if request.method == 'POST':
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            print('form validated')
            name = fm.cleaned_data['name']
            #print('Name: ', fm.cleaned_data['name'])
            #print('Email: ', fm.cleaned_data['email'])
            #print('Password: ', fm.cleaned_data['password'])
            #return render(request, 'enroll/success.html', {'nm':name})
            return HttpResponseRedirect('/reg/success')
            #fm = StudentInfo()
    else:
        fm = StudentInfo()
    return render(request, 'enroll/home.html', {'form':fm})