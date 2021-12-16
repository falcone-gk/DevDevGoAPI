from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = "articles"

router = SimpleRouter()
router.register('articles', views.ArticlesViewSet, basename='article')

urlpatterns = []

urlpatterns += router.urls
