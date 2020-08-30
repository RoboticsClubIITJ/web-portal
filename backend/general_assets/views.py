from .models import Competetion, HomeCarousel, News, UpEvents
from rest_framework import generics
from .serializers import CompetetionSerializer, HomeCarouselSerializer, NewsSerializer
from .serializers import UpEventsSerializer

class CompetetionsAPIView(generics.ListAPIView):
    queryset = Competetion.objects.all()
    serializer_class = CompetetionSerializer

class HomeCarouselAPIView(generics.ListAPIView):
    queryset = HomeCarousel.objects.all().order_by('-id')
    serializer_class = HomeCarouselSerializer

class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer

class UpEventsAPIView(generics.ListAPIView):
    queryset = UpEvents.objects.all().order_by('-date')
    serializer_class = UpEventsSerializer
