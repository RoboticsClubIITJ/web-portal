from django.middleware import csrf
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

import requests

from config.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY as CLIENT_ID
from config.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET as CLIENT_SECRET
from config.settings import LOGIN_URL as REDIRECT_URI
from config.settings import FRONTEND_URL
from .models import UserProfile
from.serializer import UserProfileSerializer


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
        if user is None:
            user = User.objects.create_user(
                email=data["email"],username=data["name"])
        login(request, user)
        return redirect(FRONTEND_URL+'/studentzone')


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
