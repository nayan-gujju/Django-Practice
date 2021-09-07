from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'nayan'
    request.session.set_expiry(60)#(0) at browser close
    return render(request ,'student/setsession.html')

def getsession(request):
    #var = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age()) 
    print(request.session.get_expiry_date()) 
    print(request.session.get_expire_at_browser_close()) 
    var = request.session.get('name',default='Guest')
    return render(request,'student/getsession.html',{'name':var})

def delsession(request):
    # 'name' in request.session:
    #del request.session['name']#this delete only data not all session 
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')