from django.shortcuts import render, HttpResponse

# Create your views here.

def setsession(request):
    request.session['name'] = 'nayan'
    return render(request ,'student/setsession.html')

def getsession(request):
    
    var = request.session['name']  
    return render(request,'student/getsession.html',{'name':var})


def delsession(request):
    # 'name' in request.session:
    #del request.session['name']#this delete only data not all session 
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')