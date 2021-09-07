from django.shortcuts import render
from signup.forms import StudentInfo

# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm = StudentInfo(request.POST)
        if fm.is_valid():
            print('Name:', fm.cleaned_data.get('name'))
            print('email:', fm.cleaned_data.get('email'))
            print('Password:', fm.cleaned_data.get('password'))
            print('Re-Password:', fm.cleaned_data.get('repassword'))

    else:
        fm = StudentInfo()
    
    return render(request, 'signup/home.html', {'form':fm})