from django import forms

class SigUpForm(forms.Form):
    username = forms.CharField(max_length=20,min_length=3)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)