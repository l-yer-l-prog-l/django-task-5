from django import forms
from .models import Answer

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['title', 'description']

        widjets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
