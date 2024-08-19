from django.contrib.auth.forms import BaseUserCreationForm
from django import forms
from django.contrib.auth.models import User

class PasswordUserCreationForm(BaseUserCreationForm):
    """Form for signing on a new user with an email address"""
    email = forms.EmailField(label='email',required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')