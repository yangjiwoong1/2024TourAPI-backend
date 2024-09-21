from django.urls import path
from .views import *
from favorites.views import *

urlpatterns = [
    path('', UserRegisterView.as_view(), name='signup'), # post - 회원가입
    path('login/', user_login_view, name='login'),
    path('refresh/', AccessTokenRefreshView.as_view(), name='token-refresh'),
    path('test-auth/', test_auth_view, name='auth-test'),
    path('username-validation/', UsernameValidationView.as_view(), name='username-validation'),
    path('nickname-validation/', NicknameValidationView.as_view(), name='nickname-validation'),
    path('<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('<str:username>/favorites/places/', PlaceView.as_view(), name='get-favorites'),
]
