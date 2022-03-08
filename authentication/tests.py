import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

from authentication.models import PreRegister

# Create your tests here.

class UserPreRegistrationCase(TestCase):
    #def setUp(self):
    #    user = PreRegister(email='testing_login@cosasdedevs.com',)
    #    user.save()

    def test_pre_registration_success(self):
        """Check if we can create an user"""

        client = APIClient()
        response = client.post(
                '/api/users/preregister', {
                'email': 'fake123@gmail.com',
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {"email":"fake123@gmail.com"})

class LoginTestUserCase(TestCase):

    def test_user_activation_failure(self):

        user = PreRegister(email='testing_login@cosasdedevs.com',)
        user.save()

        client = APIClient()
        response = client.post(
                '/api/users/', {
                'email': 'testing_login@cosasdedevs.com',
                'username': 'test_user',
                'password': 'admin123',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json.loads(response.content), {"email":"This email is not activated"})

    def test_user_registration_failure(self):

        client = APIClient()
        response = client.post(
                '/api/users/', {
                'email': 'testing_login@cosasdedevs.com',
                'username': 'test_user',
                'password': 'admin123',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json.loads(response.content), {"email":"This email is not registered"})