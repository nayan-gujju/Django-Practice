from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'nayan'
    request.session['lname'] = 'gujarati'
    return render(request ,'student/setsession.html')

def getsession(request):
    #var = request.session['name']
    var = request.session.get('name',default='Guest')
    lname = request.session.get('lname',default='Guest')
    return render(request,'student/getsession.html',{'name':var, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']#this delete only data not all session 
    return render(request,'student/delsession.html')