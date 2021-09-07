from django import forms

class StudentInfo(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()