import requests
from config.settings import API_KEY

def fetch_locationBasedList(map_x, map_y, radius, limit, page, arrange=None, content_type_id=None):
    base_url = 'http://apis.data.go.kr/B551011/ForFriTourService/locationBasedList'
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
    print(API_KEY)

    return response