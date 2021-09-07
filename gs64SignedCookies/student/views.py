from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookie(request):
    response = render(request,'student/setcookie.html')
    #response.set_cookie('name','nayan')#expire=datetime.utcnow()+timedelta(days=2)this cookie expire after 2 days
    response.set_signed_cookie('name','gujarati',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    return response

def delcookie(request):
    response = render(request,'student/delcookie.html')
    response.delete_cookie('name')
    return response
    


def getcookie(request):
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name')
    name = request.get_signed_cookie('name',default='Guest',salt='nm')#this get the default value
    
    return render(request,'student/getcookie.html',{'name':name})