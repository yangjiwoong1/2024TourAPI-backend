from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            res = {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'result': serializer.data
            }
            # 데이터를 직렬화(serializer)하여 반환
            return Response(res, status=res['status_code'], headers=headers)
        except ValidationError as e:
            # 유효성 검증(serializer.is_valid())에 대한 에러
            status_code = status.HTTP_400_BAD_REQUEST
            error_message = e.detail
        except Exception as e:
            # 기타 예외 처리
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            error_message = str(e)

        res = {
            'success': False,
            'status_code': status_code,
            'message': error_message
        }
        return Response(res, status=status_code)