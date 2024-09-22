from django.urls import path
from .views import *

urlpatterns = [
    path('places/', PlaceView.as_view(), name='create-favorite'),
    path('places/<int:placeId>/', PlaceView.as_view(), name='delete-favorite'),
]