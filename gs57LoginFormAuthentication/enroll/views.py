from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def show_data(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account has been successfully created .........')
            fm.save()
    else:  
        fm = SignupForm()

    return render(request, 'enroll/signup.html',{'form':fm})

#UserLogin Form

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            lm = AuthenticationForm(request=request, data=request.POST)
            if lm.is_valid():
                upass = lm.cleaned_data['password']
                uname = lm.cleaned_data['username']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login successfully....')
                    return HttpResponseRedirect('/profile/')

        else:
            lm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':lm})
    else:
        return HttpResponseRedirect('/profile/')

                                                                         


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')