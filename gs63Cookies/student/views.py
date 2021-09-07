from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request,'student/setcookie.html')
    #response.set_cookie('name','nayan')#expire=datetime.utcnow()+timedelta(days=2)this cookie expire after 2 days
    response.set_cookie('lname','gujarati')
    return response

def delcookie(request):
    response = render(request,'student/delcookie.html')
    response.delete_cookie('name')
    return response
    


def getcookie(request):
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name')
    name = request.COOKIES.get('name',"NGU")#this get the default value
    
    return render(request,'student/getcookie.html',{'name':name})