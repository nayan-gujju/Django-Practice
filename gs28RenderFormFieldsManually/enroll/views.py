from django.shortcuts import render
from .forms import StudentInfo
# Create your views here.

def showformdata(request):
    fm = StudentInfo(auto_id=False, label_suffix=' -', initial={'name':'Meet'})
    fm.order_fields(field_order=['email', 'first_name', 'name'])
    return render(request, 'enroll/userregistration.html', {'form':fm})