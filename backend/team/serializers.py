from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Member
from apiauth.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    techstack = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    member = ProfileSerializer(read_only=True)

    class Meta:
        model = Member
        fields = '__all__'
