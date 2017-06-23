from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from Identity.forms import UserForm
from Identity.forms import CookForm
from Identity.models import Cook


# Cooks
@login_required(login_url='/cook/sign-in/')
def home(request):
    return render(request, 'cook/home.html', {})


@login_required(login_url='/cook/sign-in/')
def cook_home(request):
    return render(request, 'base.html', {})


def cook_signup(request):
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            get_user_model().objects.create_user(**user_form.cleaned_data)
            login(request, authenticate(
                email=user_form.cleaned_data["email"],
                password=user_form.cleaned_data["password"]
            ))
            return redirect(cook_home)

    return render(request, 'cook/sign_up.html', {
        'user_form': user_form
    })


@login_required(login_url='/cook/sign-in/')
def cook_apply(request):
    cook_form = CookForm

    if request.method == "POST":
        cook_form = CookForm(request.POST, request.FILES)
        if cook_form.is_valid():
            new_cook = cook_form.save(commit=False)
            new_cook.User = request.user
            new_cook.save()
            return redirect(cook_home)

    return render(request, 'cook/apply.html', {
        'cook_form': cook_form
    })


# Helpers
def is_cook(request):
    user = request.user
    cook = Cook.objects.get(User=user)
