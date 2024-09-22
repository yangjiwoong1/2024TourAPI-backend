from django.urls import path
from .views import *

urlpatterns = [
    path('tourist-attractions/', TouristAttractionView.as_view(), name='get-attractions'),
    path('tourist-attractions/nearby/', LocationBasedTouristAttractionView.as_view(), name='get-attractions-nearby'),
    path('tourist-attractions/<int:contentId>/', TouristAttractionDetailCommonView.as_view(), name='get-attractions-detail-common'),
    path('tourist-attractions/<int:contentId>/intro/', TouristAttractionDetailIntroView.as_view(), name='get-attractions-detail-intro'),
    path('tourist-attractions/<int:contentId>/info/', TouristAttractionDetailInfoView.as_view(), name='get-attractions-detail-info'),
]