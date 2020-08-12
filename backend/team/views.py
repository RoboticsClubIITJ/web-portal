from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TeamSerializer
from .models import Member

@api_view(['GET'])
def membersList(request):
    members = Member.objects.all()
    serializer = TeamSerializer(members, many=True)
    return Response(serializer.data)