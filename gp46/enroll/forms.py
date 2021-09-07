from django import forms
from .models import User


class StudentInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        labels = {'name':'Name-', 'email':'Gmail:','password':'PPassword'}
        help_text = {'name': 'Enter your fullname'}
        error_messages = {'name':{'required':'Name is required '},
                        'email':{'required':'Email is required'}}
        widgets = {'password':forms.PasswordInput,
                'name':forms.TextInput(attrs={'placeholder':'enter your name'})}




    