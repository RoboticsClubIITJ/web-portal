from rest_framework import serializers
from team.serializers import UserSerializer
from .models import Competition, Team


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = '__all__'
        depth = 2


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = '__all__'
        depth = 2
