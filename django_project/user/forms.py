from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))