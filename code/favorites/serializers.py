from rest_framework import serializers
from .models import Place
from django.contrib.auth import get_user_model

User = get_user_model()

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'username', 'content_id', 'content_title', 'gpsX', 'gpsY']
