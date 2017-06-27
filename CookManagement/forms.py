from django import forms

from CookManagement.models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ("Cook",)
