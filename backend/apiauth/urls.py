from django.urls import path, include

from apiauth.views import AuthenticationCheckAPIView, LoginAPIView, LogoutAPIView, CsrfTokenAPIView, UserRecordView, UserDetail

app_name = 'apiauth'

urlpatterns = [
    path('csrf-token/', CsrfTokenAPIView.as_view(), name='token'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check'),
    path('user-list/', UserRecordView.as_view(), name='users-list'),
    path('user-detail/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
