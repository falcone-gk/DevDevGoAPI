from rest_framework import serializers
from .models import Article
from account.models import Profile

class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(
            source="author.get_data"
            )

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ('slug', )

