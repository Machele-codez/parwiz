from django.shortcuts import get_object_or_404

#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view
#from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
#from rest_framework.authentication import TokenAuthentication 
#from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleModelSerializer

from pprint import pprint
# Create your views here.

class ArticleViewSet(viewsets.ViewSet):
  def list(self, request):
    queryset = Article.objects.all()
    serializer = ArticleModelSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = ArticleModelSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def retrieve(self, request, pk=None):
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, pk=pk)
    serializer = ArticleModelSerializer(article)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, pk=pk)
    article.delete()
    return Response("Article Deleted")
    
  def update(self, request, pk):
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, pk=pk)
    serializer = ArticleModelSerializer(article, data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)