from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny

class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    # 어떤 유저든 접근 가능
    permission_classes = [AllowAny]

    def post(self, request):
        payload = request.data.get('payload', {})
        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        status_code = status.HTTP_201_CREATED
        res = {
            'success': "true",
            'status code': status_code,
            "user": serializer.data,
        }

        # 데이터를 직렬화(serializer)하여 반환
        return Response(res, status=status_code)
