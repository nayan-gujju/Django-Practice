from django.shortcuts import render

# Create your views here.

def fees_learn(request):
    return render(request, 'fees/feesone.html',context={'fl':'Fees for django '})