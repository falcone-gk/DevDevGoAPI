from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import PreRegister
from account.models import Profile

class PreRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreRegister
        fields = ('email',)

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, required=False, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        new_profile = Profile(user=user)
        new_profile.save()
        return user

