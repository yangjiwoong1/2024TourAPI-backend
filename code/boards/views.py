from datetime import timedelta 
from django.utils import timezone
from rest_framework import generics, permissions, status
from .models import Post, Comment, Like, Image
from .serializers import CommentSerializer, PostSerializer, LikeSerializer, PostPreviewSerializer
from rest_framework.response import Response
from django.db.models import Count,Q
import reverse_geocode
from .permissions import IsAuthorOrAdmin
from rest_framework.pagination import PageNumberPagination
from django.db import models
from rest_framework.exceptions import NotFound
areacodes = {
    "Seoul": 11,
    "Busan": 26,
    "Daegu": 27,
    "Incheon": 28,
    "Gwangju": 29,
    "Daejeon": 30,
    "Ulsan": 31,
    "Sejong": 36,
    "Gyeonggi-do": 41,
    "Chungcheongbuk-do": 43,
    "Chungcheongnam-do": 44,
    "Jeollanam-do": 46,
    "Gyeongsangbuk-do": 47,
    "Gyeongsangnam-do": 48,
    "Jeju-do": 50,
    "Gangwon-do": 51,
    "Jeollabuk-do": 52,
}


#user의 경도 위도를 받으면 areacode로 바꿔주는 함수 

def user_areacode(latitude, longitude):
    user_xy = [(latitude,longitude)]
    user_xy = reverse_geocode.search(user_xy)[0]['state']
     
    return areacodes[user_xy] 





# 수정 삭제 보기
class PostRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrAdmin]  # 수정, 삭제 권한 관리

    def retrieve(self, request, *args, **kwargs):
        post = self.get_object()

        # 조회수 증가
        post.views += 1
        post.save()
        is_author = post.author == request.user

        post_data = (
            Post.objects.annotate(
                likes_count=Count('likes'),  # 좋아요 수 집계
                comments_count=Count('comments')  # 댓글 수 집계
            )
            .filter(id=post.id)
            .first()
        )
        # 직렬화된 게시글 데이터
        serializer = self.get_serializer(post_data)
        post_response = serializer.data


        post_response["likes_count"] = post_data.likes_count
        post_response["comments_count"] = post_data.comments_count
        post_response["author_nation"] = post.author.nation
        post_response["is_author"] = is_author
        
        
       

        return Response(
            {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "게시글 조회 성공",
                "post": post_response
            },
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # PATCH 요청 시 부분 업데이트 가능
        post = self.get_object()  # 'pk'를 통해 객체를 가져옴

        title = request.data.get('title')
        content = request.data.get('content')
        area_code = request.data.get('area_code')
        images = request.FILES

        errors = {}
        if not title:
            errors['title'] = ["제목을 입력해야 합니다."]
        if not content:
            errors['content'] = ["내용을 입력해야 합니다."]
        if not area_code:
            errors['area_code'] = ["방문 지역을 선택해주세요"]

        if errors:
            return Response(
                {
                    "success": False,
                    "status_code": 400,
                    "message": errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(post, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": '게시글 수정 성공',
                    "post": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'success': False,
                'status_code': 400,
                'message': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, *args, **kwargs):
        post = self.get_object()

        # 권한 확인은 IsAuthorOrAdmin으로 처리
        self.perform_destroy(post)
        return Response(
            {
                "success": True,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "게시글 삭제 성공"
            },
            status=status.HTTP_204_NO_CONTENT
        )


#페이지네이션
class PostPagination(PageNumberPagination):
    page_size = 20  # 한 페이지에 반환할 항목 수

#인기 게시물 보기
class PopularPostListAPIView(generics.ListAPIView):
    serializer_class = PostPreviewSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        period = self.kwargs.get('period')
        now = timezone.now()

        # 기간별 시작 날짜 설정
        if period == 'daily':
            start_date = now - timedelta(days=1)
        elif period == 'weekly':
            start_date = now - timedelta(weeks=1)
        elif period == 'monthly':
            start_date = now - timedelta(days=30)
        else:
            return Post.objects.none()  # 잘못된 기간이면 빈 쿼리셋 반환
        return (
            Post.objects.annotate(
                likes_count=Count('likes'),  
                comments_count=Count('comments')
            )
            .filter(created_at__gte=start_date, likes_count__gte=10)  # 좋아요 10개 이상 필터
            .order_by('-likes_count')  # 좋아요 수 기준 정렬
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response(
                {
                    'success': "True",
                    'status_code': status.HTTP_200_OK,
                    "message": "인기 게시글 없음",
                    "popular_posts": []
                },
                status=status.HTTP_200_OK
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'success': "True",
                'status_code': status.HTTP_200_OK,
                "message": "인기 게시글 호출",
                "popular_posts": serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                'success': "True",
                'status_code': status.HTTP_200_OK,
                "message": "인기 게시글 호출",
                "popular_posts": serializer.data
            },
            status=status.HTTP_200_OK
        )

#post 전체 보기 및 생성

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostPagination
    def get_queryset(self):
        queryset = super().get_queryset()
        
        area_code = self.request.query_params.get('area_code')
        
        #필터링 
        if area_code:
            queryset = queryset.filter(area_code=area_code)

        nation = self.request.query_params.get('nation')
        if nation : 
            queryset = queryset.filter(author__nation = nation)
        search_term = self.request.query_params.get('search')
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) | Q(content__icontains=search_term) | Q(hashtags__icontains=search_term)
            )
        # Sort
        sort_by = self.request.query_params.get('sort_by', 'created_at') 
        if sort_by == 'likes':
            queryset = queryset.annotate(like_count=Count('likes')).order_by('-like_count')
        elif sort_by == 'views':
            queryset = queryset.order_by('-views')
        else:  
            queryset = queryset.order_by('-created_at')
    
        queryset = queryset.annotate(
            likes_count=Count('likes'),
            comments_count=Count('comments')
        )

        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({
                "success": "true",
                "status code": status.HTTP_200_OK,
                "message": "해당 조건에 맞는 게시물이 없습니다.",
                "posts": []
        }, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            "success": "true",
            "status code": status.HTTP_200_OK,
            "message": "게시물 목록 조회 성공",
            "posts": serializer.data  
        }, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
    # 권한 확인
        permission_classes = [IsAuthorOrAdmin]
    
    # 게시글 생성 데이터 받기
        title = request.data.get('title')
        content = request.data.get('content')
        hashtags = request.data.get('hashtags')
        area_code = request.data.get('area_code')
        images = request.FILES.getlist('images')  # 이미지 여러 개 처리 가능하게
        errors = {}
    
    # 제목과 내용 검증
        if not title:
            errors['title'] = ["제목을 입력해야 합니다."]
        if not content:
            errors['content'] = ["내용을 입력해야 합니다."]
        if not area_code: 
            errors['area_code'] = ["방문 지역을 선택해주세요"]
    
        if errors:
            return Response(
                {
                    "success": False,
                    "status_code": 400,
                    "message": errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    # 게시글 생성
        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
            hashtags=hashtags,
            area_code=area_code,
        )

    # 이미지가 있으면 저장
        if images:
            for image_url in images:
                Image.objects.create(post_id=post, image=image_url)

    # 게시글 직렬화 및 응답
        serializer = self.get_serializer(post)
        return Response(
            {
                'success': True,
                'status_code': status.HTTP_201_CREATED,   
                "message": "게시글 생성 성공",
                "post": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

#좋아요 api
class ToggleLikeAPIView(generics.GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthorOrAdmin]  # 로그인된 사용자만 접근 가능

    def post(self, request, post_id, *args, **kwargs):
        user = request.user

        # 해당 게시물 가져오기 (게시물이 없으면 NotFound 예외 발생)
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({
                "success": "false",
                "status code": status.HTTP_404_NOT_FOUND,
                "message": "게시글을 찾을 수 없음"
            }, status=status.HTTP_404_NOT_FOUND)

        # 이미 좋아요를 눌렀는지 확인
        existing_like = Like.objects.filter(post_id=post, liked_by=user)

        if existing_like.exists():
            # 좋아요가 이미 있는 경우 -> 좋아요 취소
            existing_like.delete()
            return Response({
                "success": "true",
                "status code": status.HTTP_200_OK,
                "message": "좋아요 삭제"
            }, status=status.HTTP_200_OK)
        else:
            # 좋아요가 없는 경우 -> 좋아요 추가
            try:
                Like.objects.create(post_id=post, liked_by=user)
            except Exception as e:
                return Response({
                    "success": "false",
                    "status code": status.HTTP_400_BAD_REQUEST,
                    "message": f"좋아요 생성 실패: {str(e)}"
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                "success": "true",
                "status code": status.HTTP_201_CREATED,
                "message": "좋아요 등록"
            }, status=status.HTTP_201_CREATED)
        




class CommentPagination(PageNumberPagination):
    page_size = 10  # 한 페이지에 보여줄 댓글 수


#댓글 C api

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrAdmin]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def post(self, request, post_id, *args, **kwargs):
        # 게시물 존재 여부 확인
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({
                "success": "false",
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "게시글을 찾을 수 없음"
            }, status=status.HTTP_404_NOT_FOUND)
        
        # 댓글 생성
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # author를 현재 로그인한 사용자로 설정
        serializer.save(post_id=post)  # post를 올바르게 설정
        return Response({
            "success": "true",
            "status_code": status.HTTP_201_CREATED,
            "message": "댓글 생성",
            "comment": serializer.data
        }, status=status.HTTP_201_CREATED)


    

#댓글 RUD api
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrAdmin]
    pagination_class = CommentPagination
    def get_queryset(self):
        post_id = self.kwargs['post_id']  # URL에서 post_id를 가져옴
        return Comment.objects.filter(post_id=post_id)  # 해당 게시물의 댓글만 조회

    def get(self, request, *args, **kwargs):
        comment_id = kwargs['pk']  # URL에서 comment_id를 가져옴
        try:
            comment = self.get_queryset().get(id=comment_id)  # comment_id로 조회
            serializer = self.get_serializer(comment)
            return Response({
                "success": "true",
                "status_code": status.HTTP_200_OK,
                "comment": serializer.data,
            }, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({
                "success": "false",
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "댓글을 찾을 수 없음"
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        comment_id = kwargs['pk']
        post_id = kwargs['post_id']  # 게시물 ID 가져오기
        try:
            # 특정 게시물에 속하는 댓글을 조회
            comment = self.get_queryset().filter(post_id=post_id).get(id=comment_id)
            serializer = self.get_serializer(comment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "success": "true",
                "status_code": status.HTTP_200_OK,
                "message": "댓글 수정",
                "comment": serializer.data
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "success": "false",
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "댓글을 찾을 수 없음"
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        comment_id = kwargs['pk']
        post_id = kwargs['post_id']  # 게시물 ID 가져오기
        try:
            # 특정 게시물에 속하는 댓글을 조회
            comment = self.get_queryset().filter(post_id=post_id).get(id=comment_id)
            comment.delete()
            return Response({
                "success": True,
                "status_code": status.HTTP_204_NO_CONTENT,
                "message": "댓글 삭제"
            }, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "댓글을 찾을 수 없음"
            }, status=status.HTTP_404_NOT_FOUND)