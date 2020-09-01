from rest_framework import serializers
from .models import Competition, HomeCarousel, News, UpEvents


class CompetitionSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Competition
        fields = '__all__'


class HomeCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCarousel
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class UpEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpEvents
        fields = '__all__'
