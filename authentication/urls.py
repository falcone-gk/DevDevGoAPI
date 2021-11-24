from django.urls import path

from . import views

app_name = "authentication"
urlpatterns = [
        path(
            'users/',
            views.RegistrationAPIView.as_view()
            )
        ]
