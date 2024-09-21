from django.urls import path
from .views import *

urlpatterns = [
    path('', PlanView.as_view(), name='create-plan'),
    path('destinations/', DestinationView.as_view(), name='create-destination'),
    path('<int:planId>/destinations/', DestinationView.as_view(), name='read-destinations'),
    path('destinations/<int:destinationId>/', DestinationView.as_view()),
    path('<int:planId>/', PlanView.as_view())
]
