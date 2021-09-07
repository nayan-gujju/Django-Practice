from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'myuser'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mypass'}))