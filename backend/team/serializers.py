from rest_framework import serializers
from .models import Member

class TeamSerializer(serializers.ModelSerializer):
    techstack = serializers.StringRelatedField(many=True)

    class Meta:
        model = Member
        fields = '__all__'