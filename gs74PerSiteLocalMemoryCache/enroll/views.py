from django.shortcuts import render

# Create your views here.

def user_display(request):
    return render(request, 'enroll/display.html')