from django.urls import path
from .views import UserRegisterView, user_login_view, AccessTokenRefreshView, test_auth_view

urlpatterns = [
    path('', UserRegisterView.as_view(), name='signup'), # post - 회원가입
    path('login/', user_login_view, name='login'),
    path('refresh/', AccessTokenRefreshView.as_view(), name='token-refresh'),
    path('test-auth/', test_auth_view, name='auth-test')
]
