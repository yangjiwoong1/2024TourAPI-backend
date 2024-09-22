from rest_framework import serializers
from .models import Post, Comment, Like, Image


class CommentSerializer(serializers.ModelSerializer):
    is_updated = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'is_updated']
        read_only_fields = ['author']
    def get_is_updated(self, obj):
        return obj.created_at != obj.updated_at  # 수정 여부

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user  # 로그인한 사용자로 author 필드 설정
        return super().create(validated_data)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'liked_by', 'created_at']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    is_updated = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'views', 'area_code', 'hashtags', 
                  'created_at', 'updated_at', 'is_updated', 'comments']

    def get_is_updated(self, obj):
        return obj.created_at != obj.updated_at  # 수정 여부


class PostPreviewSerializer(serializers.ModelSerializer):
    author_nickname = serializers.CharField(source='author.nickname', read_only=True)
    first_image = serializers.ImageField(source='images.first.url', allow_null=True, default=None)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['first_image', 'title', 'author_nickname', 'views', 'created_at', 'likes_count', 'comments_count']
