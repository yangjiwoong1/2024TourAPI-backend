from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import UserRegisterSerializer, UserLoginSerializer

class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    # 어떤 유저든 접근 가능
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            status_code = status.HTTP_201_CREATED
            res = {
                'success': "true",
                'status_code': status_code,
                'user': serializer.data,
            }
        else:
            status_code = status.HTTP_409_CONFLICT
            res = {
                'success': "false",
                'status_code': status_code,
                'message': serializer.errors,
            }

        # 데이터를 직렬화(serializer)하여 반환
        return Response(res, status=status_code)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login_view(request):
    serializer = UserLoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)
    if user is None:
        res = {
            'success': False,
            'status_code': status.HTTP_401_UNAUTHORIZED,
            'message': '아이디 또는 비밀번호가 일치하지 않습니다.'
        }
        return Response(res, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    refresh['username'] = user.username
    access = refresh.access_token
    access['username'] = user.username

    res = {
        'success': True,
        'status_code': status.HTTP_200_OK,
        'token': {
            'refresh_token': str(refresh),
            'access_token': str(access)
        }
    }

    return Response(res, status=status.HTTP_200_OK)

class AccessTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        access_token =  response.data.get('access', None)
        refresh_token = response.data.get('refresh', None)
        
        status_code = status.HTTP_200_OK
        res = {
            'success': True,
            'status_code': status_code,
            'token':{
                'refresh_token': refresh_token,
                'access_token': access_token
            }
        }

        return Response(res, status=status_code)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_auth_view(request):
    return Response(request.data, status=status.HTTP_200_OK)