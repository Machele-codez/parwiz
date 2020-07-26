from django.urls import path
from .views import article_list_view, article_detail

urlpatterns = [
  path('articles/', article_list_view),
  path('article/<int:pk>/', article_detail),
  ]