from django.urls import path
from . import views


urlpatterns = [
    path('', views.MembersList.as_view(), name="team-members"),
]
