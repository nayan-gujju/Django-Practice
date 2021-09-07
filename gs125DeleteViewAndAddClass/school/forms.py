from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student
        #this class in include in both create view and update view
        fields = ('name', 'email', 'password')
        widgets = {'name':forms.TextInput(attrs={'class':'namecls'}), 
        'email':forms.EmailInput(attrs={'class':'emailcls'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'passwordcls'})}
