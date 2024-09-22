from django.urls import path
from .views import *

urlpatterns = [
    path('tourist-attractions/', TouristAttractionView.as_view(), name='get-attractions'),
    path('tourist-attractions/nearby/', LocationBasedTouristAttractionView.as_view(), name='get-attractions-nearby'),
    path('tourist-attractions/<int:contentId>/', TouristAttractionDetailView.as_view(), name='get-attractions-detail'),
]