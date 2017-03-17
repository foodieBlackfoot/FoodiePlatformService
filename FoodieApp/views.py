from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from FoodieApp.forms import UserForm
from FoodieApp.forms import FoodProviderForm

# Create your views here.
def home(request):
    return redirect(foodprovider_home)

@login_required(login_url='/foodprovider/sign-in/')
def foodprovider_home(request):
    return render(request, 'foodprovider/home.html', {})

def foodprovider_signup(request):
    user_form = UserForm()
    foodprovider_form = FoodProviderForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        foodprovider_form = FoodProviderForm(request.POST, request.FILES)

        if user_form.is_valid() and foodprovider_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_foodprovider = foodprovider_form.save(commit=False)
            new_foodprovider.User = new_user
            new_foodprovider.save()
            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))
            return redirect(foodprovider_home)

    return render(request, 'foodprovider/signup.html', {
        'user_form': user_form,
        'foodprovider_form': foodprovider_form
    })
