from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token

from .serializers import ListArticleSerializer, ArticleSerializer
from .models import Article


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    lookup_field = "slug"

    def get_queryset(self):
        queryset = Article.objects.all().order_by("-created_at")
        return queryset

    def get_serializer_class(self):
        """Using differents serializers depending on request method."""

        if self.request.method == 'GET':
            return ListArticleSerializer
        return ArticleSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'articles': serializer.data,
            'articlesCount': len(serializer.data)
            }
        return Response(data)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        # Getting user id from token in headers.
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        user_id = Token.objects.get(key=token).user.profile.pk
        request.data['author'] = user_id

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        """
        Separating permissions when is a get requets with the others.
        """

        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [permissions.AllowAny,]

        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

