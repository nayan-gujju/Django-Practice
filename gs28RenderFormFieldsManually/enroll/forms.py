from django import forms

class StudentInfo(forms.Form):
    name = forms.CharField(help_text='Only 30 words')
    