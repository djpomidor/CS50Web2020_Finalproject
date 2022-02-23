from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

from .models import User

class UserForm(ModelForm):
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': "password",
        'class': "form-control",
        'name': "confirmation",
        'placeholder': "Confirm Password"
    })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "floatingInput",
                'name': "username",
                'placeholder': "Username"
            }),
            'email': EmailInput(attrs={
                'type': "email",
                'class': "form-control",
                'id': "floatingEmail",
                'name': "email",
                'placeholder': "Email Address"
            }),
            'password': PasswordInput(attrs={
                'type': "password",
                'class': "form-control",
                'id': "floatingPassword",
                'name': "password",
                'placeholder': "Password"
            }),
            }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirmation = cleaned_data.get("confirmation")

        if password != confirmation:
            self.add_error('confirmation', "Passwords does not match")
        return cleaned_data

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
