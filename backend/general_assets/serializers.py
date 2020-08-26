from rest_framework import serializers
from .models import Competetion,home_carousel,news

class CompetetionSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    class Meta:
        model = Competetion
        fields = '__all__'

class HomeCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = home_carousel
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = '__all__'
