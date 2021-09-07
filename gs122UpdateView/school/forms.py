from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ('name', 'email', 'password')
        widgets = {'name':forms.TextInput(attrs={'class':'namecls'}), 
        'email':forms.EmailInput(attrs={'class':'emailcls'}),
        'password':forms.PasswordInput(attrs={'class':'passwordcls'})}
