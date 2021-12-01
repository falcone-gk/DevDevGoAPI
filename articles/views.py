from django.contrib.auth.models import User

from rest_framework import serializers, status, viewsets
#from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token

from .serializers import ArticleSerializer
from .models import Article


class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = "slug"

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = ArticleSerializer(queryset, many=True)
        data = {
                'articles': serializer.data,
                'articlesCount': len(serializer.data)
                }
        return Response(data)

    def perform_create(self, serializer):

        token = self.request.META['Authorization'].split(' ')[1]
        user = Token.objects.get(key=token).user
        serializer.save(author=user)

    def get_permissions(self):
        """
        Separating permissions when is a get requets with the others.
        """

        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [permissions.AllowAny,]

        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

