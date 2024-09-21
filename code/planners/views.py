from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
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