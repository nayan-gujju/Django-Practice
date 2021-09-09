from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'course_template/courseone.html')

def learn_python(request):
    return render(request, 'course_template/coursetwo.html')