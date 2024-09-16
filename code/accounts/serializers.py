from .models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    # 시리얼 라이저 정의
    class Meta:
        # 사용할 모델(유효성 검증 등에 필요)
        model = User
        fields = '__all__'
        # password는 출력하지 않음
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
