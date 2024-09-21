from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Destination
from .serializers import PlanSerializer, DestinationSerializer

class PlanView(APIView):
    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'plan': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)

        res = {
            'success': False,
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    
class DestinationView(APIView):
    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'destination': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)

        res = {
            'success': False,
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, destinationId):
        try:
            destination = Destination.objects.get(pk=destinationId)
        except Destination.DoesNotExist:
            return Response({
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': '일정에 해당 목적지가 존재하지 않습니다.'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = DestinationSerializer(destination, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'destination': serializer.data
            }
            return Response(res, status=status.HTTP_200_OK)

        res = {
            'success': False,
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, destinationId):
        try:
            destination = Destination.objects.get(pk=destinationId)
            destination_data = DestinationSerializer(destination).data
            destination.delete()
            res = {
                'success': True,
                'status_code': status.HTTP_204_NO_CONTENT,
                'message': '여행지가 삭제되었습니다.',
                'deleted_destination': destination_data
            }
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except Destination.DoesNotExist:
            res = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': '해당 목적지가 존재하지 않습니다.'
            }
            return Response(res, status=status.HTTP_404_NOT_FOUND)