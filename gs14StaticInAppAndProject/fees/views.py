from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/feesone.html',{'title':'FeesPage','cname':'Django','charge':34567})