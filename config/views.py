from rest_framework import permissions
from .models import SiteConfiguration
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SiteConfigSerializer

class SiteConfigView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        serializer = SiteConfigSerializer(SiteConfiguration.get_solo())
        return Response(serializer.data)

