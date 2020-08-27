from django.middleware import csrf
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from apiauth.serializers import UserProfileSerializer, UserSerializer
from apiauth.models import UserProfile
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
import requests

from config.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY as CLIENT_ID
from config.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET as CLIENT_SECRET
from config.settings import LOGIN_URL as REDIRECT_URI


class AuthenticationCheckAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        SCOPE = 'profile+email'

        if not request.GET.get('code'):
            auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                        '&client_id={}&redirect_uri={}&scope={}').format(CLIENT_ID, REDIRECT_URI, SCOPE)
            return redirect(auth_uri)

        else:
            auth_code = request.GET.get('code')
            data = {'code': auth_code,
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'redirect_uri': REDIRECT_URI,
                    'grant_type': 'authorization_code'}
            token = requests.post('https://oauth2.googleapis.com/token', data=data)
            resp = requests.post('https://oauth2.googleapis.com/tokeninfo', data=token)

            data = resp.json()
        user  = User.objects.filter(email = data['email']).first()
        new = False ## have to add if userprofile is not udated return True
        if user is None:
            user = User.objects.create_user(
                email=data["email"],username=data["name"])
            new = True
        login(request, user)
        return Response({"message": "Successfully logged in", "user_new":new}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)


class CsrfTokenAPIView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = csrf.get_token(request)
        return Response({"csrftoken": token}, status=status.HTTP_200_OK)

class UserRecordView(APIView):
    def get(self, format=None):
        """
        Get all the user records
        :param format: Format of the user records to return to
        :return: Returns a list of user records
        """
        students = UserProfile.objects.all()
        serializer = UserProfileSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a user record
        :param format: Format of the user records to return to
        :param request: Request object for creating user
        :return: Returns a user record
        """
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404("User does not exist")

    def get(self, request, pk, format=None):
        userprofile = self.get_object(pk=pk)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userprofile = self.get_object(pk=pk)
        serializer = UserProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userprofile = self.get_object(pk=pk)
        userprofile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 
