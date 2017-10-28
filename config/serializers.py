from rest_framework import serializers
from .models import SiteConfiguration


class SiteConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteConfiguration
        fields = "__all__"