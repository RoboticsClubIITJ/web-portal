from .models import Competetion,home_carousel,news
from rest_framework import generics
from .serializers import CompetetionSerializer,HomeCarouselSerializer,NewsSerializer

class CompetetionsAPIView(generics.ListAPIView):
    queryset = Competetion.objects.all()
    serializer_class = CompetetionSerializer

class HomeCarouselAPIView(generics.ListAPIView):
    queryset = home_carousel.objects.all()
    serializer_class = HomeCarouselSerializer

class NewsAPIView(generics.ListAPIView):
    queryset = news.objects.all()
    serializer_class = NewsSerializer
