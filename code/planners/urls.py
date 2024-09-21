from django.urls import path
from .views import *

urlpatterns = [
    path('', PlanView.as_view(), name='create-plan'),
    path('destinations/', DestinationView.as_view(), name='create-destination'),
    path('destinations/<int:destinationId>/', DestinationView.as_view(), name='update-destination'),
]
