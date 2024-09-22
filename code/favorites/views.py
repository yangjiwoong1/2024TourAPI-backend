from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceSerializer
from utils import check_user_existence

class PlaceView(APIView):
    def post(self, request):
        # fk 검사(user 존재 여부), 타입 검사, 역직렬화
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'place': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)

        res = {
            'success': False,
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, username):
        user, response = check_user_existence(username)
        if not user:
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        places = Place.objects.filter(username=user)
        # many 옵션을 이용해 쿼리셋 처리
        serializer = PlaceSerializer(places, many=True)
        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'places': serializer.data
        }
        return Response(res, status=status.HTTP_200_OK)

    def delete(self, request, placeId):
        if placeId:
            try:
                place = Place.objects.get(id=placeId)
                # place 객체를 직렬화된 데이터로 반환
                place_data = PlaceSerializer(place).data
                place.delete()
                res = {
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': '즐겨찾기 항목이 삭제되었습니다.',
                    'deleted_place': place_data
                }
                return Response(res, status=status.HTTP_200_OK)
            except Place.DoesNotExist:
                res = {
                    'success': False,
                    'status_code': status.HTTP_404_NOT_FOUND,
                    'message': '해당 즐겨찾기 항목이 존재하지 않습니다.'
                }
                return Response(res, status=status.HTTP_404_NOT_FOUND)

