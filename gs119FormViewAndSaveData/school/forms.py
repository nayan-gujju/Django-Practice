from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)
    widgets = {
            'name': forms.TextInput(attrs={'class': 'inputspan','name':'name'}),
            'email': forms.TextInput(attrs={'class': 'inputspan','name':'email'}),
            'msg': forms.TextInput(attrs={'class': 'inputspan','name':'msg'}),
            }

    