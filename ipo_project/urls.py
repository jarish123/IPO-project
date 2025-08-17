from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ipo_app.views import IPOViewSet
from django.conf import settings
from django.conf.urls.static import static
from ipo_app.views import IpoListAPIView

router = DefaultRouter()
router.register(r'ipo', IPOViewSet, basename='ipo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('ipo_app.urls')),
    path('api/track-ipo/', IpoListAPIView.as_view()),
    path('api/brokers/', IpoListAPIView.as_view()),
    path('api/blogs/', IpoListAPIView.as_view()),
    path('api/blogs/<int:id>/', IpoListAPIView.as_view()),
    path('api/track-ipo/<int:id>/', IpoListAPIView.as_view()),
    path('api/brokers/<int:id>/', IpoListAPIView.as_view()),
    path('api/blogs/<int:id>/', IpoListAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)