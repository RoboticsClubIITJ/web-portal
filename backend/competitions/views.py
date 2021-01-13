from .models import Competition, Team
from rest_framework.views import APIView
from .serializers import CompetitionSerializer, TeamSerializer
from rest_framework.permissions import IsAuthenticated
from apiauth.authentication import UnsafeSessionAuthentication
from rest_framework.response import Response
from rest_framework import status, generics

import random


class RegisterAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (UnsafeSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        code = request.data.get('code')
        team_name = request.data.get('team_name')
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        comp = Competition.objects.get(id=id)
        if comp is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not comp.registration_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if code is not None:
            team = Team.objects.filter(competition=comp, code=code)
            if not team.exists():
                return Response({"data": "No such team found"}, status=status.HTTP_200_OK)
            team = team[0]
            if team.members.count() == comp.max_team:
                return Response({"data": "Team is Full"}, status=status.HTTP_200_OK)
            team.members.add(request.user)
            team.save()
            team_data = TeamSerializer(team)
            serializer = CompetitionSerializer(comp)
            return Response({"comp": serializer.data, "registered": True, "team": team_data.data},
                            status=status.HTTP_200_OK)
        if team_name is not None:
            if Team.objects.filter(name=team_name, competition=comp).exists():
                return Response({"data": "Team name Taken"}, status=status.HTTP_200_OK)
            code = 'RB' + str(comp.id) + '-' + str(request.user.id) + '-' + str(random.randint(111, 999))
            team = Team(name=team_name, code=code, competition=comp)
            team.save()
            team.members.add(request.user)
            team_data = TeamSerializer(team)
            serializer = CompetitionSerializer(comp)
            return Response({"comp": serializer.data, "registered": True, "team": team_data.data},
                            status=status.HTTP_200_OK)

        team = Team.objects.filter(competition=comp, members=request.user)
        if not team.exists():
            serializer = CompetitionSerializer(comp)
            return Response({"comp": serializer.data, "registered": False}, status=status.HTTP_200_OK)
        team_data = TeamSerializer(team[0])
        serializer = CompetitionSerializer(comp)
        return Response({"comp": serializer.data, "registered": True, "team": team_data.data},
                        status=status.HTTP_200_OK)


class CompetitionsAPIView(generics.ListAPIView):
    queryset = Competition.objects.all().order_by('-id')
    serializer_class = CompetitionSerializer
