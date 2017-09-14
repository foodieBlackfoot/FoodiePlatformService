import json

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken

from Identity.models import Cook
from CookManagement.models import Meal, Order, OrderDetail
from api.customer.serializers import CookSerializer, MealSerializer

STATUS_FAILURE = "failed"


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


@csrf_exempt
def customer_add_order(request):
    """
    :params:
        access_token
        cook_id
        address
        order_details (json format), example:
            [{"meal_id": 1, "quality": 2}]
    :return:
        {"status": "success}
    """

    if request.method == "POST":
        # Get token
        access_token = AccessToken.objects.get(token=request.POST.get(
            "access_token"), expires__gt=timezone.now())

        # Get profile
        customer = access_token.user.customer

        # Check address
        if not request.POST["address"]:
            generate_response(STATUS_FAILURE, "Address is required.")

        # Check orderDetails
        order_details = json.loads(request.POST["order_details"])
        if len(order_details) == 0:
            generate_response(STATUS_FAILURE, "order_details is empty.")

        # Get order total price
        order_total = 0
        for meal in order_details:
            order_total += Meal.objects.get(id=meal["meal_id"]).Price * meal[
                "quantity"]

        # Create an order
        order = Order.objects.create(
            Customer=customer,
            Cook_id=request.POST["cook_id"],
            Address=request.POST["address"],
            TotalPrice=order_total,
            Status=Order.CREATED
        )

        # Create order_detail
        for meal in order_details:
            OrderDetail.objects.create(
                Order=order,
                Meal_id=meal["meal_id"],  # TODO: validate meal
                Quantity=meal["quantity"],
                SubTotalPrice=Meal.objects.get(id=meal["meal_id"]).Price *
                              meal["quantity"]
            )

            return JsonResponse({"status": "success"})


def customer_get_latest_order(reqeust):
    return JsonResponse({})


def generate_response(status, error_message=None):
    if error_message is None:
        return JsonResponse({"status": status})
    return JsonResponse({"status": status, "error": error_message})
