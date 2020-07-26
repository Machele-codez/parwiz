from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Article
from .serializers import ArticleModelSerializer

from pprint import pprint
# Create your views here.

@csrf_exempt # this allows posts to this view without a csrf token
def article_list_view(request):
  
  if request.method == 'GET':
    """
    View list of all ariticles
    """
    articles = Article.objects.all()
    serializer = ArticleModelSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)
    
  elif request.method == 'POST':
    """
    adding an article
    """
    data = JSONParser().parse(request) #parse the request into a python dict
    pprint(data)
    serializer = ArticleModelSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    
    return JsonResponse(serializer.errors, status=400) 
    

@csrf_exempt
def article_detail(request, pk):
  try:
    article = Article.objects.get(pk=pk)
  except Article.DoesNotExist:
    return HttpResponse("Requested Article Does Not Exist", status=404)
    
  if request.method == 'GET':
    """
    article detail
    """
    serializer = ArticleModelSerializer(article)
    return JsonResponse(serializer.data)
    
  elif request.method == 'PUT':
    """
    update an article
    """
    data = JSONParser().parse(request)
    serializer = ArticleModelSerializer(article, data=data)
    
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
  
  elif request.method == 'DELETE':
    """
    delete an article
    """
    article_title = article.title
    article.delete()
    return HttpResponse(f"{article_title} deleted!", status=204)