from rest_framework import serializers
from .models import Member
from user.models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'roll_number', 'year', 'email', 'phone', 'avatar']

class TeamSerializer(serializers.ModelSerializer):
    techstack = serializers.StringRelatedField(many=True)
    member = ProfileSerializer(read_only=True)

    class Meta:
        model = Member
        fields = '__all__'