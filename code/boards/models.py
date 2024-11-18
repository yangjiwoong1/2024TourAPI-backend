from django.db import models
from django.conf import settings


##글
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE)  
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    area_code = models.IntegerField(null=True, blank=True)
    hashtags = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'글쓴이 : {self.author} 제목 : {self.title}'
    

## 댓글
class Comment(models.Model):    
    post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username',on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'글 제목 : {self.post.title} 댓글 작성자 : {self.author.username}'


## 좋아요
class Like(models.Model):
    post_id = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)  # 연결된 게시물
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 좋아요 누른 날짜

    def __str__(self):
        return f'좋아요한 사용자 : {self.liked_by.username} 좋아요한 게시물 : {self.post.title}'


##이미지
class Image(models.Model):
    post_id = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)  # 연결된 게시물
    image = models.ImageField(upload_to='image/',null=True, blank = True)  # 이미지 URL

    def __str__(self):
        return f'post 제목 {self.post.title}'