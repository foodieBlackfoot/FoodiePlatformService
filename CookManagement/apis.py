from django.http import JsonResponse

from Identity.models import Cook
from CookManagement.serializers import CookSerializer


def customer_get_cooks(request):
    cook = CookSerializer(
        Cook.objects.all().order_by("-id"),
        many=True,
        context={"request": request}
    ).data

    return JsonResponse({"cooks": cook})
