from rest_framework import serializers
from .models import Place
from django.contrib.auth import get_user_model

User = get_user_model()

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'username', 'content_id', 'content_title', 'gpsX', 'gpsY']

    def validate(self, data):
        username = data.get('username')
        content_id = data.get('content_id')

        if Place.objects.filter(username__username=username, content_id=content_id).exists():
            raise serializers.ValidationError({"content_id": "이미 존재하는 즐겨찾기 입니다."})

        return data