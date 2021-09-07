from django import forms


class Student(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(error_messages={'required':'Enter Your Email'},min_length=10, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter Your Email'},min_length=10, max_length=100)






    