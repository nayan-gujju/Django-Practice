from django import forms
from django.core import validators

def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should be start with s........')

class StudentInfo(forms.Form):
    #this is built in validators
    name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)]) 
    #this is custom validators
    email = forms.EmailField(validators=[start_with_s])
    
    
    
    