from django import forms

class StudentInfo(forms.Form):
    name = forms.CharField() 
    
    email = forms.EmailField()
    
    
    
    def clean(self):
        cleaned_data = super().clean()

        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more then or equal 4 characters')
        
        valemail = self.cleaned_data['email']
        if len(valemail) < 10:
            raise forms.ValidationError('Enter Email more then or equal 10 characters')

        