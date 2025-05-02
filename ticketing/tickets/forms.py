from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label=True)
    password = forms.CharField(widget=forms.PasswordInput)