# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IPOViewSet
from ipo_app.views import IpoListAPIView
from .views import LoginAPIView




router = DefaultRouter()
router.register(r'ipo', IPOViewSet, basename='ipo')

urlpatterns = [
    path(' ', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api/track-ipo/', IpoListAPIView.as_view()),
    path('api/brokers/', IpoListAPIView.as_view()),
    path('api/blogs/', IpoListAPIView.as_view()),
    path('api/blogs/<int:id>/', IpoListAPIView.as_view()), 

]