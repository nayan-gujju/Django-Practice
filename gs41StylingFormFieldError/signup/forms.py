from django import forms


class StudentInfo(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter your Name'},max_length=50, min_length=5)
    email = forms.EmailField(error_messages={'required':'Enter your Email'},max_length=50, min_length=10)
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your Password'},max_length=50,min_length=10)  