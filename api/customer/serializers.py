from rest_framework import serializers

from Identity.models import Cook
from CookManagement.models import Meal


class CookSerializer(serializers.ModelSerializer):
    Logo = serializers.SerializerMethodField()

    def get_Logo(self, cook):
        request = self.context.get('request')
        logo_url = cook.Logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = Cook
        fields = (
            "id", "Name", "Description", "Rating", "Tag", "Address", "Phone",
            "Logo")


class MealSerializer(serializers.ModelSerializer):
    Image = serializers.SerializerMethodField()

    def get_Image(self, meal):
        request = self.context.get('request')
        image_url = meal.Image.url
        return request.build_absolute_uri(image_url)

    class Meta:
        model = Meal
        fields = ("id", "Name", "Description", "Image", "Price")
