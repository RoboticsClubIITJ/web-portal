from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from .serializers import TeamSerializer
from .models import Member


class MembersList(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = TeamSerializer
    search_fields = ['member__user__first_name', 'member__user__last_name', 'member__techstack__tech_name']
    filter_backends = (SearchFilter,)
