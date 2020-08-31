from django.urls import path
from . import views


urlpatterns = [
    path('homeview', views.HomeTeamList.as_view(), name="team-homeview"),
    path('', views.MembersList.as_view(), name="team-members"),
]
