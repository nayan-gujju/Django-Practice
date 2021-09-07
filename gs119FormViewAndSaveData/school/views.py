from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm
from .models import Contact
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.


class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name':'nayan'}
    def form_valid(self, form):
        print(form)
        x = form.cleaned_data['name']
        y = form.cleaned_data['email']
        z = form.cleaned_data['msg']
        ss = Contact(name=x,email=y,msg=z)
        ss.save()
        return super().form_valid(form)




class ThankTemplateView(TemplateView):
    template_name = 'school/thankyou.html'