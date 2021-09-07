from django import forms
from enroll.models import Student_Info
class Student(forms.ModelForm):
    class Meta:
        model = Student_Info
        fields = ('name', 'email', 'password')
        labels = {'name':'Name-', 'email':'Gmail:','password':'PPassword'}
        help_text = {'name': 'Enter your fullname'}
        error_messages = {'name':{'required':'Name is required '},
                        'email':{'required':'Email is required'}}
        widgets = {'password':forms.PasswordInput,
                'name':forms.TextInput(attrs={'placeholder':'enter your name'})}