from django.shortcuts import render
from enroll.forms import SignUp, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import Group, User

# Create your views here.


#Signup view function
def user_signup(request):
    if request.method == 'POST':
        fm = SignUp(request.POST)
        if fm.is_valid():
            messages.success(
                request, 'Your account has been successfully created........')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
    else:
        fm = SignUp()

    return render(request, 'enroll/signup.html', {'form': fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            lm = AuthenticationForm(request=request, data=request.POST)
            if lm.is_valid():
                uname = lm.cleaned_data['username']
                upass = lm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Ypur are logged in....')
                    return HttpResponseRedirect('/dashboard/')

        else:
            lm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': lm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


