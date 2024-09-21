from django.urls import path
from .views import *

urlpatterns = [
    path('tourist-attractions/', TouristAttractionView.as_view(), name='get-attractions'),
]