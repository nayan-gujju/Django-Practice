from django import forms


class StudentInfo(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valrepass = self.cleaned_data['repassword']
    
        if valpass != valrepass:
            raise forms.ValidationError('Password is not match......')
