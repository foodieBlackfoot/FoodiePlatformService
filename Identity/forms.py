from django import forms
from django.contrib.auth import get_user_model
from Identity.models import Cook, Customer


class UserForm(forms.ModelForm):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ("email", "password",)


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("Name", "Description", "Tag", "Address", "Phone", "Logo")


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("Avatar", "Phone", "Address")
