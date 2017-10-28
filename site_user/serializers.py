from rest_framework import serializers
from .models import SiteUser, Contact, Skill, Experience, Education, Project


class SiteUserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    class Meta:
        model = SiteUser
        exclude = ["id", ]

    def get_photo(self, obj):
        request = self.context.get('request')
        photo = obj.photo.url
        return request.build_absolute_uri(photo)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ["id", ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ["id", ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ["id", ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ["id", ]
