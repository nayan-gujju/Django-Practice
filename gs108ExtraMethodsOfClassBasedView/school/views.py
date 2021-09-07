from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import ContactInfo

# Create your views here.

def home(request):
    return render(request, 'school/home.html')


class MyHomeView(View):
    def get(self, request):
        return render(request, 'school/home.html')

##########################################



def aboutfun(request):
    context  = {'msg':'Welcome to Globalia Function Based View'}
    return render(request, 'school/about.html', context)

class MyAboutView(View):
    def get(self, request):
        context = {'msg':'Welcome to Globalia Class Based View '}    
        return render(request, 'school/about.html', context)

#########################################

def contactfun(request):
    if request.method == 'POST':
        form = ContactInfo(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for submitted....')
    else:
        form = ContactInfo()
    return render(request, 'school/form.html', {'form':form})


class ContactForm(View):

    def get(self, request):
        form = ContactInfo()
        return render(request, 'school/form.html', {'form':form})

    def post(self, request):
        form = ContactInfo(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for submitted....')

###########################################################################


def newsfun(request, template_name):
    template_name = template_name
    context  = {'msg':'Breaking News Of Function Based View'}
    return render(request, template_name, context)


class NewsClass(View):
    def get(self, request, template_name):
        self.template_name = template_name
        context  = {'msg':'Breaking News Of Class Based View'}
        return render(request,self.template_name, context)