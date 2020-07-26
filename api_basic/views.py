from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse 

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleModelSerializer

from pprint import pprint
# Create your views here.

@api_view(['GET', 'POST'])# this enables full rest_framework view functionality (web browsable api)
def article_list_view(request):
  
  if request.method == 'GET':
    """
    View list of all ariticles
    """
    articles = Article.objects.all()
    serializer = ArticleModelSerializer(articles, many=True)
    return Response(serializer.data)
    
  elif request.method == 'POST':
    """
    adding an article
    """
    data = request.data #already parsed
    pprint(data)
    serializer = ArticleModelSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
  try:
    article = Article.objects.get(pk=pk)
  except Article.DoesNotExist:
    return HttpResponse("Requested Article Does Not Exist", status=status.HTTP_404_NOT_FOUND)
    
  if request.method == 'GET':
    """
    article detail
    """
    serializer = ArticleModelSerializer(article)
    return Response(serializer.data)
    
  elif request.method == 'PUT':
    """
    update an article
    """
    data = request.data
    serializer = ArticleModelSerializer(article, data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    """
    delete an article
    """
    article_title = article.title
    article.delete()
    return Response(f"{article_title} deleted!", status=status.HTTP_204_NO_CONTENT)