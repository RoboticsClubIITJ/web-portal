from django.urls import path
from . import views


urlpatterns = [
    path('get/', views.CompetitionsAPIView.as_view(), name="competitions"),
    path('register/', views.RegisterAPIView.as_view(), name="register"),
]
