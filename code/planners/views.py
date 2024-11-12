from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Plan, Destination
from .serializers import PlanSerializer, DestinationSerializer
from collections import defaultdict
from utils import check_user_existence

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
    
    def get(self, request, username):
        user, response = check_user_existence(username)
        if not user:
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        search_query = request.GET.get('search', '')

        plans = Plan.objects.filter(creator=user).filter(title__icontains=search_query)
        serializer = PlanSerializer(plans, many=True)

        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'plans': serializer.data
        }
        return Response(res, status=status.HTTP_200_OK)
    
    def patch(self, request, planId):
        try:
            plan = Plan.objects.get(pk=planId)
        except Plan.DoesNotExist:
            return Response({
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': '플래너가 존재하지 않습니다.'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = PlanSerializer(plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'plan': serializer.data
            }
            return Response(res, status=status.HTTP_200_OK)

        res = {
            'success': False,
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, planId):
        try:
            plan = Plan.objects.get(pk=planId)
            plan.delete()
            res = {
                'success': True,
                'status_code': status.HTTP_204_NO_CONTENT,
                'message': '플래너가 삭제되었습니다.'
            }
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except Plan.DoesNotExist:
            return Response({
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': '플래너가 존재하지 않습니다.'
            }, status=status.HTTP_404_NOT_FOUND)

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
    
    def get(self, request, planId):
        if not Plan.objects.filter(id=planId).exists():
            return Response({
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': '해당 플랜이 존재하지 않습니다.'
            }, status=status.HTTP_404_NOT_FOUND)

        destinations = Destination.objects.filter(plan_id=planId)
        serializer = DestinationSerializer(destinations, many=True)
        
        grouped_by_visit_date = defaultdict(list)
        for item in serializer.data:
            visit_date = item['visit_date']
            grouped_by_visit_date[visit_date].append(item)

        grouped_destinations = [{'visit_date': visit_date, 'destinations': destinations}
                                for visit_date, destinations in grouped_by_visit_date.items()]

        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'result': grouped_destinations
        }
        return Response(res, status=status.HTTP_200_OK)

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