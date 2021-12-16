from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PreRegister
from .serializers import PreRegisterSerializer, UserSerializer
# Create your views here.

class PreRegisterAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PreRegisterSerializer

class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        # Check if email exists in PreRegister model
        if not PreRegister.objects.filter(email=request.data['email']).exists():
            message = {'email': 'This email is not registered'}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        # Check if email has been activated by an admin
        elif not PreRegister.objects.get(email=request.data['email']).is_activated():
            message = {'email': 'This email is not activated'}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        # Check if request data is valid and saving in model
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email},
                status=status.HTTP_200_OK
                )

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
