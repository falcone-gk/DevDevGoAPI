from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.tag


class Article(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)

    description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    # Every article must have an author. This will answer questions like "Who
    # gets credit for writing this article?" and "Who can edit this article?".
    # Unlike the `User` <-> `Profile` relationship, this is a simple foreign
    # key (or one-to-many) relationship. In this case, one `Profile` can have
    # many `Article`s.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles'
    )

    tags = models.ManyToManyField(
        Tag, related_name='articles'
    )

    def __str__(self):
        return self.title

