from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from CookManagement.forms import MealForm, CookFormForEdit
from CookManagement.models import Meal


@login_required(login_url='/cook/sign-in/')
def cook_account(request):
    cook_form = CookFormForEdit(instance=request.user.cook)

    if request.method == "POST":
        cook_form = CookFormForEdit(request.POST,
                                    request.FILES,
                                    instance=request.user.cook)
        if cook_form.is_valid():
            cook_form.save()

    return render(request, 'account.html', {
        "cook_form": cook_form
    })


# Create your views here.
@login_required(login_url='/cook/sign-in/')
def cook_menu(request):
    meals = Meal.objects.filter(Cook=request.user.cook).order_by("-id")
    return render(request, 'menu.html', {"meals": meals})


@login_required(login_url='/cook/sign-in/')
def cook_add_meal(request):
    add_meal_form = MealForm

    if request.method == "POST":
        add_meal_form = MealForm(request.POST, request.FILES)
        if add_meal_form.is_valid():
            meal = add_meal_form.save(commit=False)
            print(request)
            meal.Cook = request.user.cook
            meal.save()
            return redirect(cook_menu)

    return render(request, 'add_meal.html', {
        "form": add_meal_form
    })


@login_required(login_url='/cook/sign-in/')
def cook_edit_meal(request, meal_id):
    meal_instance = Meal.objects.get(id=meal_id)
    edit_meal_form = MealForm(instance=Meal.objects.get(id=meal_id))

    if request.method == "POST":
        edit_meal_form = MealForm(request.POST, request.FILES,
                                  instance=Meal.objects.get(id=meal_id))
        if edit_meal_form.is_valid():
            edit_meal_form.save()
            return redirect(cook_menu)

    if meal_instance.Image:
        edit_meal_form.fields['Image'].required = False
    return render(request, 'edit_meal.html', {
        "form": edit_meal_form
    })


@login_required(login_url='/cook/sign-in/')
def cook_order(request):
    return render(request, 'order.html', {})


@login_required(login_url='/cook/sign-in/')
def cook_report(request):
    return render(request, 'report.html', {})
