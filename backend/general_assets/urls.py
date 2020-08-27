from django.urls import path
from . import views


urlpatterns = [
    path('competetions/', views.CompetetionsAPIView.as_view(), name="competetions-api-overview"),
    path('carousel/', views.HomeCarouselAPIView.as_view(), name="carousel-api-overview"),
    path('news/', views.NewsAPIView.as_view(), name="news-api-overview"),
]
