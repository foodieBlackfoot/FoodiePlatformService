from django import forms
from django.contrib.auth.models import User
from FoodieApp.models import Cook

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("Name", "Description", "Tag", "Address", "Phone", "Logo")
