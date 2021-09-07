from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

'''def home(request):
    mv = cache.get('movie', 'has_expired')
    if mv == 'has_expired':
        cache.set('movie', 'The end', 30)
        mv = cache.get('movie')
    return render(request, 'enroll/course.html', {'fm':mv})'''

""" def home(request):
    mv = cache.get_or_set('fees',405450,20, version=2)
    return render(request, 'enroll/course.html', {'fm':mv}) """

""" def home(request):
    data = {'name':'ngu', 'roll':170220107019}
    cache.set_many(data, 60)
    mv = cache.get_many(data)
    print(mv)
    return render(request, 'enroll/course.html', {'fm':mv}) """

"""def home(request):
    cache.delete('fees',version=1)
    return render(request, 'enroll/course.html')"""

""" def home(request):
    mv = cache.decr('no', delta=1)
    print(mv)
    return render(request, 'enroll/course.html',{'fm':mv}) """

def home(request):
    cache.clear()
    return render(request, 'enroll/course.html')