from rest_framework import serializers

from Identity.models import Cook


class CookSerializer(serializers.ModelSerializer):
    Logo = serializers.SerializerMethodField()

    def get_Logo(self, cook):
        request = self.context.get('request')
        logo_url = cook.Logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = Cook
        fields = (
            "Name", "Description", "Rating", "Tag", "Address", "Phone", "Logo")
