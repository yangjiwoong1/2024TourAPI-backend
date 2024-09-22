from django.urls import path
from .views import (
    PostDetailView,
    PostUpdateDeleteAPIView,
    PostCreateAPIView,
    PopularPostListAPIView,
    PostListView,
    ToggleLikeAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # 전체 게시물 목록
    path('create/', PostCreateAPIView.as_view(), name='post-create'),  # 게시물 생성
    path('popular/<str:period>/', PopularPostListAPIView.as_view(), name='popular-posts'),  # 인기 게시물 목록
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # 게시물 상세 조회
    path('<int:pk>/update/', PostUpdateDeleteAPIView.as_view(), name='post-update'),  # 게시물 수정 patch
    path('<int:pk>/delete/', PostUpdateDeleteAPIView.as_view(), name='post-delete'),  # 게시물 삭제 delete
    path('<int:post_id>/like/', ToggleLikeAPIView.as_view(), name='toggle-like'),  # 좋아요 추가/제거
    path('<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),  # 댓글 목록 및 생성
    path('<int:post_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),  # 댓글 상세 조회, 수정, 삭제
]
