import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .B551011_EngService1.services import *

class TouristAttractionView(APIView):
    def get(self, request):
        search = request.GET.get('search', '') # 필수
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        areacode = request.GET.get('areacode', None)

        response = fetch_searchKeyword1(search, limit, page, areacode)

        try:
            response.raise_for_status()
            data = response.json()
            if data.get("response", {}).get("body", {}).get("items", {}):
                items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
            else:
                items = []
        except requests.HTTPError as http_err:
            return Response({
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'HTTP 에러 발생: {http_err}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            return Response({
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'에러 발생: {err}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        filtered_items = [
            {
                'title': item.get('title'),
                'mapx': item.get('mapx'),
                'mapy': item.get('mapy'),
                'contentid': item.get('contenttypeid'),
                'addr1': item.get('addr1'),
                'areacode': item.get('areacode'),
                'firstimage2': item.get('firstimage2'),
                'modifiedtime': item.get('modifiedtime'),
                'tel': item.get('tel')
            }
            for item in items
        ]

        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'results': filtered_items
        }
        return Response(res, status=status.HTTP_200_OK)
