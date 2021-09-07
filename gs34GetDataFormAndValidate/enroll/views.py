from django.shortcuts import render
from .forms import StudentInfo 
# Create your views here.
def showmoredata(request):
    if request.method == 'POST':
        fm = StudentInfo(request.POST)
        print(fm)
        if fm.is_valid():
            print('Form Validated...')
            print('Name-',request.POST['name'])
            print('Email-',fm.cleaned_data['email'])
            print('Password: ',fm.cleaned_data['password'])
            fm = StudentInfo()
    else:
        fm = StudentInfo()
    
    return render(request, 'enroll/home.html', {'form':fm})