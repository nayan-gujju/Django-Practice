from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'nayan'
    return render(request ,'student/setsession.html')

def getsession(request):
    #var = request.session['name']
    var = request.session.get('name',default='Guest')
    return render(request,'student/getsession.html',{'name':var})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')