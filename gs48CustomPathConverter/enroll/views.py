from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'enroll/home.html')


def show_details(request, my_id):
    return render(request, 'enroll/show.html', {'id':my_id})

def show_subdetails(request, my_id, my_subid):
    if my_id == 1111 and my_subid == 5:

        student={'id':my_id ,'name':'Meet'}
    if my_id == 2222 and my_subid == 6:

        student={'id':my_id, 'name':'Meet2'}
    if my_id == 3333 and my_subid == 7:    

        student={'id':my_id,'name':'Meet3'}
    return render(request, 'enroll/show.html', student)