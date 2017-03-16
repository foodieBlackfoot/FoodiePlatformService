from django import forms
from django.contrib.auth.models import User
from FoodieApp.models import FoodProvider

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name")

class FoodProviderForm(forms.ModelForm):
    class Meta:
        model = FoodProvider
        fields = ("Name", "Description", "Tag", "Address", "Phone", "Email", "Logo")
