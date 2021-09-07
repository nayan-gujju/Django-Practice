from django.shortcuts import render

# Create your views here.

def learn_django(request):
    cname = 'Django'
    duration = '4 months'
    seats = 10
    course_details = {'nm':cname, 'du':duration, 'st':seats}
    return render(request, 'courseone.html', course_details)