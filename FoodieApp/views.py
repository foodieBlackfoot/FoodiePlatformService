from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
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
    return render(request, 'foodprovider/signup.html', {
        'user_form': user_form,
        'foodprovider_form': foodprovider_form
    })
