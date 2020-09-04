from .models import Competition, HomeCarousel, News, UpEvents
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CompetitionSerializer, HomeCarouselSerializer, NewsSerializer
from .serializers import UpEventsSerializer

from apiauth.models import UserProfile, TechStack


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


class ProfileSelectListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = {}
        data['stacks'] = [{'text': stack.tech_name} for stack in TechStack.objects.all()]
        data['gender'] = [{'text': y, 'value': x} for x, y in UserProfile.GENDER_CHOICES]
        data['prog'] = [{'text': y, 'value': x} for x, y in UserProfile.PROG_CHOICES]
        data['branch'] = [{'text': y, 'value': x} for x, y in UserProfile.BRANCH_CHOICES]
        data['year'] = [{'text': y, 'value': x} for x, y in UserProfile.YEAR_CHOICES]
        return Response(data, status=status.HTTP_200_OK)
