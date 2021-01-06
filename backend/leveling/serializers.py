from rest_framework import serializers
from .models import Level, Submission


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = ('response_link',)


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
