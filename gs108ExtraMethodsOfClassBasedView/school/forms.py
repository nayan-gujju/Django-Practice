from django import forms


class ContactInfo(forms.Form):
    name = forms.CharField(max_length=40)