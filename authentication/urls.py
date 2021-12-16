from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = "authentication"
urlpatterns = [
        path(
            'user/<int:pk>',
            views.UserRetrieveUpdateAPIView.as_view(),
            name='retrieve_update_user'
            ),
        path(
            'users/preregister',
            views.PreRegisterAPIView.as_view(),
            name='preregister_user'
            ),
        path(
            'users/',
            views.RegistrationAPIView.as_view(),
            name='register_user'
            ),
        path(
            'users/login',
            views.LoginAPIView.as_view(),
            name='login_user'
            ),
        ]
