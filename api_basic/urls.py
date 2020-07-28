from django.urls import path, include

from .views import ArticleViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')


urlpatterns = [
  path('viewsets/', include(router.urls)),
  path('viewsets/<int:pk>', include(router.urls)),
  ]