from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class LoginForm(ModelForm):
#     # password = django.forms.PasswordInput()
#     # class Meta:
#     #     model = User
#     #     fields = ["username", "password"]

# authentication/forms.py
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
