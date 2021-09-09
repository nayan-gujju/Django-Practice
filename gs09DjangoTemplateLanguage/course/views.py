from django.shortcuts import render

# Create your views here.

def learn_django(request):
    cname = 'django is a lunguage'
    duration =  '4 Months'
    fee = 56.2356
    course_dic = {'nm':cname, 'du':duration, 'fe':fee}
    return render(request, 'course/courseone.html', context=course_dic)