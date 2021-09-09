from django.shortcuts import render

# Create your views here.
def learn_if(request):
    return render(request, 'if/ifone.html',{'nm':'Django','st':5})