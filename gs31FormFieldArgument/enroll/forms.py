from django import forms

class StudentInfo(forms.Form):
    name = forms.CharField(label='Your name ', label_suffix=' -', initial='Meet', required=False, disabled=True,help_text='Limit of 10 words')
