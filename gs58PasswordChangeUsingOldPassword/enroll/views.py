from django.shortcuts import render
from enroll.forms import SignUp
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.

#Signup view function
def user_signup(request):
    if request.method == 'POST':
        fm  = SignUp(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account has been successfully created........')
            fm.save()
    else:
        fm = SignUp()

    return render(request,'enroll/signup.html',{'form':fm})


#Login Form

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
                    messages.success(request,'Ypur are logged in....')
                    return HttpResponseRedirect('/profile/')
       
        else:
            lm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':lm})
    else:
        return HttpResponseRedirect('/profile/')


#

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#change password with old password

def ch_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password successfully changed...')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')