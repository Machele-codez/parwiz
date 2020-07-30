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

class ArticleViewSet(viewsets.ModelViewSet):
  """
  provides all the default .create .list .retrieve , etc. methods
  """
  serializer_class = ArticleModelSerializer
  queryset = Article.objects.all()
  