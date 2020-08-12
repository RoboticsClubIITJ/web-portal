from django.urls import path
from . import views


urlpatterns = [
    path('', views.membersList, name="team-members"),
]