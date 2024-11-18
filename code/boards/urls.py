from django.urls import path
from .views import (
    PopularPostListAPIView,
    PostListView,
    ToggleLikeAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    PostRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list-create'),  # 전체 게시물 목록 조회 및 생성
    path('popular/<str:period>/', PopularPostListAPIView.as_view(), name='popular-posts'),  # 인기 게시물 목록
    path('<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view(), name='post-detail-update-delete'),  # 게시물 상세 조회
    path('<int:post_id>/like/', ToggleLikeAPIView.as_view(), name='toggle-like'),  # 좋아요 추가/제거
    path('<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),  # 댓글 목록 및 생성
    path('<int:post_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),  # 댓글 상세 조회, 수정, 삭제
]
