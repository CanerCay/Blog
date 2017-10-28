from rest_framework import permissions
from .models import SiteUser, Skill, Experience, Education, Project
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SiteUserSerializer, ContactSerializer, SkillSerializer, ExperienceSerializer, \
    EducationSerializer, ProjectSerializer
from rest_framework import response, status, generics


class SiteUserView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        serializer = SiteUserSerializer(SiteUser.get_solo(), context={'request': request})
        return Response(serializer.data)


class ContactView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return self.is_valid(serializer)
        return self.is_invalid(serializer)

    def is_invalid(self, serializer):
        return response.Response(
            data=serializer.errors,
            status=status.HTTP_200_OK,
        )

    def is_valid(self, serializer):
        serializer.save()
        return response.Response(
            data={'data': True},
            status=status.HTTP_201_CREATED,
        )


class SkillListView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = SkillSerializer


class ExperienceListView(generics.ListCreateAPIView):
    queryset = Experience.objects.all().order_by("-start_date")
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ExperienceSerializer


class EducationListView(generics.ListCreateAPIView):
    queryset = Education.objects.all().order_by("-start_date")
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EducationSerializer


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProjectSerializer
