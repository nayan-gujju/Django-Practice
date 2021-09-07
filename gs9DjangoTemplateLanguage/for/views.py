from django.shortcuts import render

# Create your views here.
def learn_for(request):
    student = {'names':['meet','nayan','jt','dallu']}
    return render(request, 'for/forone.html', student)

def learn_fort(request):
    stu = {'stu1':{'name': 'nayan', 'roll':101},
            'stu2':{'name': 'meet', 'roll':102},
            'stu3':{'name': 'dallu', 'roll':103},
            'stu4':{'name': 'jt', 'roll':104},
        }
    student1 = {'student1':stu}
    return render(request, 'for/fortwo.html', student1)