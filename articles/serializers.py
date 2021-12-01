from rest_framework import serializers
from .models import Article

class ListArticleSerializer(serializers.ModelSerializer):
    """Serializer to show when a get request is send to API."""

    author = serializers.ReadOnlyField(
            source="author.get_data"
            )

    class Meta:
        model = Article
        read_only_fields = ('slug', )
        exclude = ('id',)

class ArticleSerializer(serializers.ModelSerializer):
    """Serializer used to post and put request."""

    class Meta:
        model = Article
        fields = ('title', 'description', 'body', 'author')