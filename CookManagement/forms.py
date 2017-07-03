from django import forms

from CookManagement.models import Meal
from Identity.models import Cook


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ("Cook",)


class CookFormForEdit(forms.ModelForm):
    email = forms.EmailField(label="E-mail")

    class Meta:
        model = Cook
        fields = ("Name", "Description", "Tag", "Address", "Phone", "Logo")


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("Name", "Description", "Tag", "Address", "Phone", "Logo")