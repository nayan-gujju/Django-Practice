from django.shortcuts import render
from enroll.forms import SignupForm
from django.contrib import messages
# Create your views here.

def show_data(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
        messages.success(request, 'Your account has been successfully created...')
    else:
        fm = SignupForm()

    return render(request, 'enroll/signup.html', {'form':fm})
