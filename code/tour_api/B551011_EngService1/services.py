import requests
from config.settings import API_KEY

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
    print(API_KEY)

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
        'mapinfoYN': 'Y'
    }

    response = requests.get(base_url, params=params)
    print(API_KEY)

    return response