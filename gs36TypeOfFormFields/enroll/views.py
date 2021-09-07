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
            print('Roll No.:', fm.cleaned_data['roll'])
            print('Price:', fm.cleaned_data['price'])
            print('Rate:', fm.cleaned_data['rate'])
            print('Agree:', fm.cleaned_data['agree'])
            print("Comments:", fm.cleaned_data['comment'])
            print("Email:", fm.cleaned_data['email'])
            print('Website:', fm.cleaned_data['website'])
            print('Password:', fm.cleaned_data['password'])
            print('Notes:', fm.cleaned_data['notes'])

    else:
        fm = StudentInfo()
    return render(request, 'enroll/home.html', {'form':fm})