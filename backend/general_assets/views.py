from .models import Competition, HomeCarousel, News, UpEvents
from rest_framework import generics
from .serializers import CompetitionSerializer, HomeCarouselSerializer, NewsSerializer
from .serializers import UpEventsSerializer


class CompetitionsAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class HomeCarouselAPIView(generics.ListAPIView):
    queryset = HomeCarousel.objects.all().order_by('-id')
    serializer_class = HomeCarouselSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer


class UpEventsAPIView(generics.ListAPIView):
    queryset = UpEvents.objects.all().order_by('-date')
    serializer_class = UpEventsSerializer
