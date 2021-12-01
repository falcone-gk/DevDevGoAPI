from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer

class ProfileRetrieveAPIView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
