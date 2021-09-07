from django import forms
from .models import User
class Student(forms.ModelForm):
    class Meta:
        model = User
       # fields = ('name', 'email', 'password')
       # fields = '__all__'
        exclude = ['name']
