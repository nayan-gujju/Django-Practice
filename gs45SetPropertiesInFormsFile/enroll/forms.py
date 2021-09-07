from django import forms
from .models import User


class StudentInfo(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True)
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        labels = {'name':'Name-', 'email':'Gmail:','password':'PPassword'}
       
        widgets = {'password':forms.PasswordInput}




    