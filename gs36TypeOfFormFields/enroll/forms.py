from django import forms

class StudentInfo(forms.Form):
    name = forms.CharField(min_length=5, max_length=150,strip=False,empty_value='MEETMMO',error_messages={'required': 'enter your Name'} )
    roll = forms.IntegerField(min_value=5,max_value=10)
    price = forms.DecimalField(min_value=5, max_value=40, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=0, max_value=5)
    agree = forms.BooleanField(label_suffix=" ",label='I Agree')    
    comment = forms.SlugField()
    email = forms.EmailField(max_length=25)
    website = forms.URLField()
    password = forms.CharField(widget=forms.PasswordInput)
    notes = forms.CharField(widget=forms.Textarea(attrs={'row':5 , 'cols':30}))