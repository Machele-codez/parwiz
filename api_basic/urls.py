from django.urls import path
from .views import ArticleGenericAPIView


urlpatterns = [
  path('generic/articles/', ArticleGenericAPIView.as_view()),
  path('generic/articles/<int:id>/', ArticleGenericAPIView.as_view()),
  ]