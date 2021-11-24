from django.contrib.auth.models import User

from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
# Create your views here.

class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
