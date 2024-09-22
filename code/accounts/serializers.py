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

class UsernameValidationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)

    def validate_username(self, value):
        # 150자 제한은 CharField에서 처리
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("존재하는 ID입니다.")
        return value
    
class NicknameValidationSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=100, required=True)

    def validate_nickname(self, value):
        if User.objects.filter(nickname=value).exists():
            raise serializers.ValidationError("존재하는 닉네임입니다.")
        return value
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'nation']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nation', 'nickname']