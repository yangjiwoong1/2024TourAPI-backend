from django.contrib import admin
from .models import Post, Comment, Like, Image

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Image)