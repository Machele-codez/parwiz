from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse 

#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view
#from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleModelSerializer

from pprint import pprint
# Create your views here.

class ArticleGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
  """
  The view would have its request methods take in an optional id argument so as to allow one view to handle both single object and multiple object operations via two URLs. 
  """
  
  serializer_class = ArticleModelSerializer
  queryset = Article.objects.all()
  
  lookup_field = 'id'#field used to retrieve model instance 
  
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get(self, request, id=None):
    if id:
      return self.retrieve(request, id) #gets single object using id
      
    return self.list(request) #gets list of all objects in queryset
  
  def post(self, request):
    return self.create(request) #create view from mixins.CreateModelMixin
  
  def put(self, request, id):
    return self.update(request, id) #update instance
    
  def delete(self, request, id):
    return self.destroy(request, id) #delete an instance
  