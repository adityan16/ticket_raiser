from django import forms
from .models import Ticket


class LoginForm(forms.Form):
    email = forms.EmailField(label=True)
    password = forms.CharField(widget=forms.PasswordInput)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['project_name', 'title', 'description', 'priority']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4})
        }
        