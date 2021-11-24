from django.urls import path

from . import views

app_name = 'profile'
urlpatterns = [
        path(
            'profiles/<slug:username>',
            views.ProfileRetrieveAPIView.as_view()
            ),
        path(
            'profiles/<slug:username>/follow',
            views.ProfileFollowAPIView.as_view()
            ),
        ]
