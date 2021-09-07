from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'nayan'
    request.session['lname'] = 'gujarati'
    return render(request ,'student/setsession.html')

def getsession(request):
    #var = request.session['name']
    var = request.session.get('name',default='Guest')
    key = request.session.keys()
    item = request.session.items()
    age = request.session.setdefault('age', '21')
    return render(request,'student/getsession.html',{'name':var,'keys':key,'items':item,'age':age })

def delsession(request):
    # 'name' in request.session:
    #del request.session['name']#this delete only data not all session 
    request.session.flush()
    return render(request,'student/delsession.html')