from .models import Department, Submission
from rest_framework.views import APIView
from .serializers import LevelSerializer, SubmissionSerializer
from django.views.decorators.cache import never_cache
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from apiauth.authentication import UnsafeSessionAuthentication
from rest_framework.response import Response
from rest_framework import status


class DepartmentsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (UnsafeSessionAuthentication,)

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        deps = Department.objects.all()
        data = {}
        for dep in deps:
            data[dep.name] = []
            for level in dep.levels.all():
                lk = LevelSerializer(level).data
                subs = Submission.objects.filter(user=request.user, level=level)
                if len(subs) > 0:
                    l_sub = subs.last()
                    lk['status'] = l_sub.status
                data[dep.name].append(lk)
        return Response({"departments": data}, status=status.HTTP_200_OK)


class SubmissionsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (UnsafeSessionAuthentication,)

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        us_deps = Department.objects.filter(coordinators=request.user)
        levels = []
        for dep in us_deps:
            for level in dep.levels.all():
                levels.append(level.id)
        subs = Submission.objects.filter(status='Pending', level__in=levels)
        data = SubmissionSerializer(subs, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        us_deps = Department.objects.filter(coordinators=request.user)
        if len(us_deps) == 0:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {}
        for key in request.data.keys():
            data[key] = request.data.get(key)
        id = int(data.get('id'))
        comment = data.get('comment')
        status_p = data.get('status')
        sb = Submission.objects.filter(id=id)
        if len(sb) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        sb = sb.first()
        if status_p is not None:
            sb.status = status_p
        if comment is not None:
            sb.comment = comment
        sb.save()
        return Response(status=status.HTTP_200_OK)
