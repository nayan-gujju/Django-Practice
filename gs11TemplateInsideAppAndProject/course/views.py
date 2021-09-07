from django.shortcuts import render

# Create your views here.

def learn_course(request):
    return render(request, 'course/courseone.html', context={'cn':'learn Django'})