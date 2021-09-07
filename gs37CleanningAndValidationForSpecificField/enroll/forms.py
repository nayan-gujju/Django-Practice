from django import forms

class StudentInfo(forms.Form):
    name = forms.CharField() 
    
    email = forms.EmailField()
    
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more then or equal 4 characters')
        return valname