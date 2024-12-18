import requests
from config.settings.base import API_KEY

def fetch_searchKeyword1(keyword, limit, page, areacode=None, content_type_id=None):
    base_url = 'http://apis.data.go.kr/B551011/EngService1/searchKeyword1'
    params = {
        'serviceKey': API_KEY,
        'numOfRows': limit,
        'pageNo': page,
        'MobileOS': 'AND',
        'MobileApp': 'Welcome',
        '_type': 'json',
        'keyword': keyword
    }

    if areacode:
        params['areaCode'] = areacode

    if content_type_id:
        params['contentTypeId'] = content_type_id

    response = requests.get(base_url, params=params)

    return response

def fetch_detailCommon1(contentId, limit, page):
    base_url = 'http://apis.data.go.kr/B551011/EngService1/detailCommon1'
    params = {
        'serviceKey': API_KEY,
        'numOfRows': limit,
        'pageNo': page,
        'MobileOS': 'AND',
        'MobileApp': 'Welcome',
        '_type': 'json',
        'contentId': contentId,
        'defaultYN': 'Y',
        'firstImageYN': 'Y',
        'areacodeYN': 'Y',
        'addrinfoYN': 'Y',
        'mapinfoYN': 'Y',
        'overviewYN': 'Y'
    }

    response = requests.get(base_url, params=params)

    return response

def fetch_locationBasedList1(map_x, map_y, radius, limit, page, arrange=None, content_type_id=None):
    base_url = 'http://apis.data.go.kr/B551011/EngService1/locationBasedList1'
    params = {
        'serviceKey': API_KEY,
        'numOfRows': limit,
        'pageNo': page,
        'MobileOS': 'AND',
        'MobileApp': 'Welcome',
        '_type': 'json',
        'mapX': map_x,
        'mapY': map_y,
        'radius': radius
    }

    if arrange:
        params['arrange'] = arrange

    if content_type_id:
        params['contentTypeId'] = content_type_id

    response = requests.get(base_url, params=params)

    return response

def fetch_detailIntro1(contentId, content_type_id, limit, page):
    base_url = 'http://apis.data.go.kr/B551011/EngService1/detailIntro1'
    params = {
        'serviceKey': API_KEY,
        'numOfRows': limit,
        'pageNo': page,
        'MobileOS': 'AND',
        'MobileApp': 'Welcome',
        '_type': 'json',
        'contentId': contentId,
        'contentTypeId': content_type_id
    }

    response = requests.get(base_url, params=params)

    return response

def fetch_detailInfo1(contentId, content_type_id, limit, page):
    base_url = 'http://apis.data.go.kr/B551011/EngService1/detailInfo1'
    params = {
        'serviceKey': API_KEY,
        'numOfRows': limit,
        'pageNo': page,
        'MobileOS': 'AND',
        'MobileApp': 'Welcome',
        '_type': 'json',
        'contentId': contentId,
        'contentTypeId': content_type_id
    }

    response = requests.get(base_url, params=params)

    return response
