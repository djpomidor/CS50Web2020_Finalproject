from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput, ModelChoiceField, DateInput
from django.db import models


from .models import *

class UserForm(ModelForm):
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': "password",
        'class': "form-control",
        'name': "confirmation",
        'placeholder': "Confirm Password"
    })
    )

    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="(Nothing)", widget=forms.Select(attrs={
        'class': "form-select",
        'placeholder': "Choose",
        'id': "floatingInput",
        'autocomplete': "off"
    })
    )
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['name'].queryset = Company.objects.all()

    class Meta:
        model = User
        fields = ['username', 'company', 'email', 'password', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "floatingInput",
                'name': "username",
                'placeholder': "Username"
            }),
#            'company': forms.Select(attrs={
#                'type': "text",
#                'class': "form-select",
#                'id': "floatingInput",
#                'placeholder': "Chooooos"
#            }),
            'first_name': TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "floatingInput",
                'name': "first_name",
                'placeholder': "First Name"
            }),
            'last_name': TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "floatingInput",
                'name': "last_name",
                'placeholder': "Last Name"
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

class CompanyForm(ModelForm):
#    phone = PhoneNumberField(widget=forms.TextInput(attrs={'type': "tel", 'class': "form-control", 'id': "floatingInput",'name': "phone", 'placeholder': "Phone number"}))

    class Meta:
        model = Company
        fields = ['name', 'address', 'city', 'postal_code', 'country', 'email', 'phone']
        widgets = {
            'name': TextInput(attrs={'type': "text", 'class': "form-control", 'id': "floatingInput",'name': "name", 'placeholder': "Company name"}),
            'address': TextInput(attrs={'type': "text", 'class': "form-control", 'id': "floatingInput",'name': "adress", 'placeholder': "Adress"}),
            'city': TextInput(attrs={'type': "text", 'class': "form-control", 'id': "floatingInput",'name': "city", 'placeholder': "City"}),
            'postal_code': NumberInput(attrs={'type': "number", 'class': "form-control", 'id': "floatingInput",'name': "postal_code", 'placeholder': "Postal code"}),
            'country': TextInput(attrs={'type': "text", 'class': "form-control", 'id': "floatingInput",'name': "country", 'placeholder': "Country"}),
            'email': EmailInput(attrs={'type': "email", 'class': "form-control", 'id': "floatingInput",'name': "email", 'placeholder': "Email"}),
            'phone': TextInput(attrs={'type': "tel", 'class': "form-control", 'id': "floatingInput",'name': "phone", 'placeholder': "Phone number"}),
            }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'type', 'circulation', 'binding', 'width', 'height', 'due_date', 'delivery_date']
        widgets = {
            'name': TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'name': "name",
                'placeholder': "Order name"
            }),
            'type': forms.Select(attrs={
                'type': "text",
                'class': "form-select",
                'name': "name",
                'placeholder': "Book, magazin, ets."
            }),
            'circulation': TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'name': "circulation",
                'placeholder': "Circulation"
            }),
            'binding': forms.Select(attrs={
                'type': "text",
                'class': "form-select",
                'name': "binding",
                'placeholder': "Binding style"
            }),
            'width': NumberInput(attrs={
                'type': "text",
                'class': "form-control",
                'name': "width",
                'placeholder': "width"
            }),
            'height': NumberInput(attrs={
                'type': "text",
                'class': "form-control",
                'name': "height",
                'placeholder': "height"
            }),
            'due_date': DateInput(attrs={
                'type': "text",
                'class': "form-control flatpickr-input",
                'placeholder': "Select date"
            }),
            'delivery_date': DateInput(attrs={
                'type': "text",
                'class': "form-control flatpickr-input",
                'placeholder': "Select date"
            })

            }

############################################################################
class OrderPartsForm(ModelForm):
    class Meta:
        model = Part
        fields = ['part_name', 'pages', 'paper', 'color', 'laminate']
        widgets = {
            'part_name': TextInput(attrs={
                'type': "hidden",
                'class': "form-select",
                'name': "part_name",
                'placeholder': "Aaaa",
            }),
            'pages': NumberInput(attrs={
                'type': "text",
                'class': "form-control",
                'name': "pages",
                'placeholder': "Number of pages..."
            }),
            'paper': forms.Select(attrs={
                'type': "text",
                'class': "form-control",
                'name': "",
                'placeholder': "Select paper..."
            }),
            'color': forms.Select(attrs={
                'type': "text",
                'class': "form-control",
                'name': "color",
                'placeholder': "color"
            }),
            'laminate': forms.Select(attrs={
                'type': "text",
                'class': "form-select",
                'name': "laminate",
                'placeholder': ""
            }),
            }
