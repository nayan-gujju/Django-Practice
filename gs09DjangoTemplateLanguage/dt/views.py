from django.shortcuts import render
from datetime import datetime
# Create your views here.

def date_time(request):
    d = datetime.now()
    return render(request, 'dt/datetime.html',{'ddtt':d})