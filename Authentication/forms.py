from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class CreateUserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-8 rounded-xl",
        "type": "text",
        "placeholder": "Username"
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "text",
        "placeholder": "Full name"
    }))

    institution = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "text",
        "placeholder": "Institution"
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "email",
        "placeholder": "Email"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "password",
        "placeholder": "Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "password",
        "placeholder": "Confirm Password"
    }))

    

    class Meta:
        model = User
        fields = ['first_name', 'institution', 'email',
                  'username', 'password1', 'password2']