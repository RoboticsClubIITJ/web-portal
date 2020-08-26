from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('project-list/', views.projectList, name="project-list"),
    path('project-detail/<str:pk>/', views.projectDetail, name="project-detail"),
]
