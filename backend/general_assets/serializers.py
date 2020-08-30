from rest_framework import serializers
from .models import Competetion, HomeCarousel, News, UpEvents 

class CompetetionSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    class Meta:
        model = Competetion
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
