from django.urls import path
from . import views


urlpatterns = [
    path('departments/', views.DepartmentsAPIView.as_view(), name="departments-api-overview"),
    path('review/submissions', views.SubmissionsAPIView.as_view(), name="departments-api-overview"),
]
