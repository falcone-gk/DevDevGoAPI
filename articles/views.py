from django.contrib.auth.models import User

from rest_framework import serializers, status, viewsets
#from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleSerializer
from .models import Article


class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
