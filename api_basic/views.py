from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse 

#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleModelSerializer

from pprint import pprint
# Create your views here.

class ArticleListAPIView(APIView):
  def get(self, request):
    articles = Article.objects.all()
    serializer = ArticleModelSerializer(articles, many=True)
    return Response(serializer.data)
    
  def post(self, request):
    data = request.data
    serializer = ArticleModelSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

class ArticleDetailAPIView(APIView):
  def get_object(self, id):
    """
    this method returns a single instance of the model if found.
    note that if the requested instance is not found then a Response object is returned which would raise errors if passed in as data to a serializer.
    """
    try:
      return Article.objects.get(id=id)
    except Article.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
  def get(self, request, id):
    article = self.get_object(id)
    serializer = ArticleModelSerializer(article)
    return Response(serializer.data)
    
  def put(self, request, id):
    article = self.get_object(id)
    serializer = ArticleModelSerializer(article, data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request, id):
    article = self.get_object(id)
    article.delete()
    return Response("Article deleted", status=status.HTTP_204_NO_CONTENT)