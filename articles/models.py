from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from account.models import Profile

# Create your models here.
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
        Profile, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

