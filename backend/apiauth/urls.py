from django.urls import path

from .views import AuthenticationCheckAPIView, LoginAPIView, LogoutAPIView, CsrfTokenAPIView

app_name = 'apiauth'

urlpatterns = [
    path('csrf-token/', CsrfTokenAPIView.as_view(), name='token'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')
]
