from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/cook/sign-in/')
def cook_account(request):
    return render(request, 'account.html', {})


# Create your views here.
@login_required(login_url='/cook/sign-in/')
def cook_meal(request):
    return render(request, 'meal.html', {})


@login_required(login_url='/cook/sign-in/')
def cook_add_meal(request):
    return render(request, 'add_meal.html')


@login_required(login_url='/cook/sign-in/')
def cook_order(request):
    return render(request, 'order.html', {})


@login_required(login_url='/cook/sign-in/')
def cook_report(request):
    return render(request, 'report.html', {})
