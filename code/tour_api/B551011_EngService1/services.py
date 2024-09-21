import requests
from config.settings import API_KEY

def fetch_searchKeyword1(keyword, limit, page, areacode=None):
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

    response = requests.get(base_url, params=params)
    print(API_KEY)

    return response
