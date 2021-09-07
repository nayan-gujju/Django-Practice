from django import forms
from .models import User

class StudentInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']