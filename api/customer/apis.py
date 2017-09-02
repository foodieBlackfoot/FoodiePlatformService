from django.http import JsonResponse

from Identity.models import Cook
from CookManagement.models import Meal
from api.customer.serializers import CookSerializer, MealSerializer


def customer_get_cooks(request):
    cooks = CookSerializer(
        Cook.objects.all().order_by("-id"),
        many=True,
        context={"request": request}
    ).data
    return JsonResponse({"cooks": cooks})


def customer_get_meals(request, cook_id):
    meals = MealSerializer(
        Meal.objects.filter(Cook_id=cook_id).order_by("-id"),
        many=True,
        context={"request": request}
    ).data
    return JsonResponse({"meals": meals})


def customer_add_order(reqeust):
    return JsonResponse({})


def customer_get_latest_order(reqeust):
    return JsonResponse({})
