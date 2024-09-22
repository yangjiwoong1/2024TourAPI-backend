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
        content_type_id = request.GET.get('contentTypeId', None)

        response = fetch_searchKeyword1(search, limit, page, areacode, content_type_id)

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
                'contentid': item.get('contentid'),
                'contenttypeid': item.get('contenttypeid'),
                'title': item.get('title'),
                'tel': item.get('tel'),
                'modifiedtime': item.get('modifiedtime'),
                'firstimage2': item.get('firstimage2'),
                'areacode': item.get('areacode'),
                'sigungucode': item.get('sigungucode'),
                'addr1': item.get('addr1'),
                'mapx': item.get('mapx'),
                'mapy': item.get('mapy')
            }
            for item in items
        ]

        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'results': filtered_items
        }
        return Response(res, status=status.HTTP_200_OK)

class TouristAttractionDetailView(APIView):
    def get(self, request, contentId):
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)

        response = fetch_detailCommon1(contentId, limit, page)

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
                'contentid': item.get('contentid'),
                'contenttypeid': item.get('contenttypeid'),
                'title': item.get('title'),
                'tel': item.get('tel'),
                'homepage': item.get('homepage'),
                'modifiedtime': item.get('modifiedtime'),
                'firstimage': item.get('firstimage'),
                'firstimage2': item.get('firstimage2'),
                'areacode': item.get('areacode'),
                'sigungucode': item.get('sigungucode'),
                'addr1': item.get('addr1'),
                'addr2': item.get('addr2'),
                'zipcode': item.get('zipcode'),
                'mapx': item.get('mapx'),
                'mapy': item.get('mapy'),
                'overview': item.get('overview'),
            }
            for item in items
        ]
        
        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'results': filtered_items
        }
        return Response(res, status=status.HTTP_200_OK)

class LocationBasedTouristAttractionView(APIView):
    def get(self, request):
        map_x = request.GET.get('mapX') # required
        map_y = request.GET.get('mapY') # required
        radius = request.GET.get('radius') # required
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        arrange = request.GET.get('arrange', None)
        content_type_id = request.GET.get('contentTypeId', None)

        response = fetch_locationBasedList1(map_x, map_y, radius, limit, page, arrange, content_type_id)

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
                'contentid': item.get('contentid'),
                'contenttypeid': item.get('contenttypeid'),
                'title': item.get('title'),
                'dist': item.get('dist'),
                'tel': item.get('tel'),
                'modifiedtime': item.get('modifiedtime'),
                'firstimage2': item.get('firstimage2'),
                'areacode': item.get('areacode'),
                'sigungucode': item.get('sigungucode'),
                'addr1': item.get('addr1'),
                'mapx': item.get('mapx'),
                'mapy': item.get('mapy')
            }
            for item in items
        ]

        res = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'results': filtered_items
        }
        return Response(res, status=status.HTTP_200_OK)