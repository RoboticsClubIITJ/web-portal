from rest_framework import serializers
from .models import Project, Member


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'