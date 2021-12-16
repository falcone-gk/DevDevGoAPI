import django_heroku
import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['devdevgo-api.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dd5n8sprc7ehil',
        'USER': 'droyomacikxohq',
        'PASSWORD': os.environ["DATABASE_PASSWORD"],
        'HOST': 'ec2-3-89-214-80.compute-1.amazonaws.com',
        'PORT':  '5432'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

CORS_ALLOWED_ORIGINS = [
    "https://devdevgo.me",
]

# Activate Django-Heroku.
django_heroku.settings(locals())
