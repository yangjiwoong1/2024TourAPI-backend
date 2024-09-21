from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

def check_user_existence(username):
    try:
        user = User.objects.get(username=username)
        return user, None
    except User.DoesNotExist:
        return None, {
            'success': False,
            'status_code': status.HTTP_404_NOT_FOUND,
            'message': '사용자를 찾을 수 없습니다.'
        }