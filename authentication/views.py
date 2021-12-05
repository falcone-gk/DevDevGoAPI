from django.contrib.auth.models import User

from rest_framework import serializers, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
# Create your views here.

class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class LoginAPIView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        })

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
