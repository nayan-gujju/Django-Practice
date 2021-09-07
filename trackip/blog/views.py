from django.shortcuts import render, HttpResponseRedirect
from blog.forms import Contact
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.

#Home Page
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html', {'posts':posts})

#About Page
def about(request):
    return render(request,'blog/about.html')

#Contact Page
def contact(request):
    fm = Contact()
    return render(request, 'blog/contact.html', {'form':fm})

#Dashboard Page
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip', 0)
        return render(request, 'blog/dashboard.html', {'posts':posts,'fname':full_name,'groups':gps, 'ip':ip})
    else:
        return HttpResponseRedirect('/login/')

#Login Page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None: 
                    login(request, user)
                    messages.success(request, 'Logged in successfully....')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

#LogOut Page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    

#Signup Page
def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Congratulations!!  Your have become an author.....')
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        fm = SignupForm()
    return render(request, 'blog/signup.html',{'form':fm})

#Add New Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                description = fm.cleaned_data['description']
                pst = Post(title=title, description=description)
                pst.save()
                fm = PostForm()
        else:
            fm = PostForm()
        return render(request, 'blog/addpost.html', {'form':fm})
    else:
        return HttpResponseRedirect("/login/")

#Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")

#Delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect("/login/")


