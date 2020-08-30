from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .models import Project


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/project-list',
        'Detail': '/project-detail/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projectDetail(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
