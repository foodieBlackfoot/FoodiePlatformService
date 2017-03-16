from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect(foodprovider_home)

@login_required(login_url='/foodprovider/sign-in/')
def foodprovider_home(request):
    return render(request, 'foodprovider/home.html')
