from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from FoodieApp.forms import UserForm
from FoodieApp.forms import CookForm

# Create your views here.
def home(request):
    return redirect(cook_home)

@login_required(login_url='/cook/sign-in/')
def cook_home(request):
    return render(request, 'cook/base.html', {})

@login_required(login_url='/cook/sign-in/')
def cook_account(request):
    return render(request, 'cook/account.html', {})

@login_required(login_url='/cook/sign-in/')
def cook_meal(request):
    return render(request, 'cook/meal.html', {})

@login_required(login_url='/cook/sign-in/')
def cook_order(request):
    return render(request, 'cook/order.html', {})

@login_required(login_url='/cook/sign-in/')
def cook_report(request):
    return render(request, 'cook/report.html', {})

def cook_signup(request):
    user_form = UserForm()
    cook_form = CookForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        cook_form = CookForm(request.POST, request.FILES)

        if user_form.is_valid() and cook_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_cook = cook_form.save(commit=False)
            new_cook.User = new_user
            new_cook.save()
            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))
            return redirect(cook_home)

    return render(request, 'cook/sign_up.html', {
        'user_form': user_form,
        'cook_form': cook_form
    })
