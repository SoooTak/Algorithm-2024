import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getCtyCodeList'

params ={
        'serviceKey' : 'WwUx24zXj59TFZvpPVxkBRIJJe5LllIGnz99n0p/JNGjtRd7jUwhWHY0OXrkIyDfuhi/J5Mbn1eeYIiO4rjE6A==',
         '_type' : 'xml'
        }

def get_city_code(city_name):
    city_code = None
    city_type = None
    # 도시 유형 딕셔너리를 만듭니다.
    city_types = {
        "부산": "광역시",
        "인천": "광역시",
        "대구": "광역시",
        "대전": "광역시",
        "광주": "광역시",
        "울산": "광역시",
        "서울": "특별시",  #없음
        "세종": "특별시"
    }

    if city_name in city_types:
        city_type = city_types[city_name]
    else:
        city_type = "시"
    try :    
        city_code_response = requests.get(url, params=params)
        city_code_response.raise_for_status()
        city_code_soup = BeautifulSoup(city_code_response.text, 'xml')
        
        city_elements = city_code_soup.find_all('item')
        for city_element in city_elements :
            if city_element.find('cityname').text == city_name + city_type :
                city_code = city_element.find('citycode').text
                break
    
    except Exception as e :
        print(f'오류 발생 : {e}')
    
    return city_code, city_type
    

def get_route_id(city_code, route_number):
    route_id = None
    route_id_url = 'http://apis.data.go.kr/1613000/BusRouteInfoInqireService/getRouteNoList'
    route_id_params = {
        'serviceKey': 'WwUx24zXj59TFZvpPVxkBRIJJe5LllIGnz99n0p/JNGjtRd7jUwhWHY0OXrkIyDfuhi/J5Mbn1eeYIiO4rjE6A==',
        '_type': 'xml',
        'cityCode': city_code,
        'routeNo': route_number
    }
    try :
        route_id_response = requests.get(route_id_url, params=route_id_params)
        route_id_response.raise_for_status()
        route_id_soup = BeautifulSoup(route_id_response.text, 'xml')
        route_id_element = route_id_soup.find('routeid')
        if route_id_element :
            route_id = route_id_element.text
    
    except Exception as e :
        print(f"버스번호 조회 오류  : {e}")
    
    return route_id
    
city_name = str(input("도시 이름 : "))
route_number = str(input("버스 번호 : "))
city_code, city_type = get_city_code(city_name)
if city_code:
    route_id = get_route_id(city_code, route_number)
    print(f'Route ID: {route_id}, City Code: {city_code}, City Type: {city_type}')
else:
    print('City code could not be retrieved.')
