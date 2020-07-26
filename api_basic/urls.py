from django.urls import path
from .views import ArticleDetailAPIView, ArticleListAPIView
urlpatterns = [
  path('articles/', ArticleListAPIView.as_view()),
  path('article/<int:id>/', ArticleDetailAPIView.as_view()),
  ]