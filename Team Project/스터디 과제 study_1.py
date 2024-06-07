import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
url = 'https://apis.data.go.kr/1613000/BusSttnInfoInqireService/getCtyCodeList'
params = {
    'serviceKey': 'NI9pDLpfb3/7YUQsHOwHKHmy0wHB0LruCc/wJ6Zt+qWR5JPnZdavOjSCJ6bOgpCc0LMAOVQETq4XNYxneKyrEg==',
    '_type': 'xml'
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
        "서울": "특별시",  # 없음
        "세종": "특별시"
    }

    if city_name in city_types:
        city_type = city_types[city_name]
    else:
        city_type = "시"


    try:
        city_code_response = requests.get(url, params=params)  # api요청을 보냄
        city_code_response.raise_for_status()  # HTTP 오류가 발생한 경우 예외 발생
        city_code_soup = BeautifulSoup(city_code_response.text, 'xml')  # xml로 보낸 파일을 추출

        city_elements = city_code_soup.find_all('item')  # 받은 xml 파일에서 item 이라는 태그를 가진 모든것을 추출
        for city_element in city_elements:
            if city_element.find('cityname').text == city_name + city_type:  # 광역시/특별시, 일반 시 구분하는 코드
                city_code = city_element.find('citycode').text  # 도시 코드 xml에서 찾아서 city_code에 넣어줌
                break
    except Exception as e:
        print(f'도시 코드 조회 중 오류가 발생했습니다: {e}')
    
    return city_code, city_type


def get_route_id(city_code, route_number):
    route_id = None
    route_id_url = 'http://apis.data.go.kr/1613000/BusRouteInfoInqireService/getRouteNoList'
    route_id_params = {
        'serviceKey': 'NI9pDLpfb3/7YUQsHOwHKHmy0wHB0LruCc/wJ6Zt+qWR5JPnZdavOjSCJ6bOgpCc0LMAOVQETq4XNYxneKyrEg==',
        '_type': 'xml',
        'cityCode': city_code,
        'routeNo': route_number
    }

    try:
        route_id_response = requests.get(route_id_url, params=route_id_params)
        route_id_response.raise_for_status()  # HTTP 오류가 발생한 경우 예외 발생
        route_id_soup = BeautifulSoup(route_id_response.text, 'xml')
        route_id_element = route_id_soup.find('routeid')
        if route_id_element:
            route_id = route_id_element.text
    except Exception as e:
        print(f'노선번호 조회 중 오류가 발생했습니다: {e}')
    return route_id



def print_via_stops(city_code, route_id):
    via_stops = []  # 경유 정류장을 저장할 리스트
    params = {
        'serviceKey': 'NI9pDLpfb3/7YUQsHOwHKHmy0wHB0LruCc/wJ6Zt+qWR5JPnZdavOjSCJ6bOgpCc0LMAOVQETq4XNYxneKyrEg==',
        'numOfRows': 800,
        'pageNo': 1,
        '_type': 'xml',
        'cityCode': city_code,  # 도시 코드 설정
        'routeId': route_id  # 노선 ID 설정
    }
    base_url = 'http://apis.data.go.kr/1613000/BusRouteInfoInqireService/getRouteAcctoThrghSttnList'
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.text
        root = ET.fromstring(data)
        prev_stop = None  # 이전 정류장 초기화
        a = 0
        print('----------경유 정류장----------')
        for item in root.iter('item'):
            nodenm_element = item.find('nodenm')
            updowncd_element = item.find('updowncd')
            if nodenm_element is not None:
                current_stop = nodenm_element.text
                updowncd = int(updowncd_element.text) if updowncd_element is not None else None
                
                if prev_stop == current_stop:  # 이전 정류장과 현재 정류장이 같은지 확인
                    print('----------회차----------')
                    print(current_stop)
                else:
                    a += 1
                    via_stops.append((current_stop, updowncd))  # 경유 정류장과 updowncd를 목록에 추가
                    if updowncd is not None:
                        print(f"{a}. {current_stop} (updowncd: {updowncd})")  # 현재 정류장과 updowncd 출력
                    else:
                        print(f"{a}. {current_stop}")  # 현재 정류장 출력
                prev_stop = current_stop  # 현재 정류장을 이전 정류장으로 업데이트
        print('----------경유 정류장----------')
    else:
        print(f'API 호출 실패 (응답 코드: {response.status_code})')
        print(response.text)  # 오류 응답 데이터 출력
    
    return via_stops  # 경유 정류장 목록 반환

def get_station_id(city_code, nodenm):
    url = 'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getSttnNoList'
    params = {
        'serviceKey': 'NI9pDLpfb3/7YUQsHOwHKHmy0wHB0LruCc/wJ6Zt+qWR5JPnZdavOjSCJ6bOgpCc0LMAOVQETq4XNYxneKyrEg==',
        'pageNo': 1,
        'numOfRows': 100,  # 더 많은 결과를 검색하기 위해 값 조정
        '_type': 'xml',
        'cityCode': city_code,
        'nodeNm': nodenm
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        # Find the station with the exact same name
        for item in root.iter('item'):
            current_nodenm = item.find('nodenm').text
            if current_nodenm == nodenm:  # Check if the names match exactly
                nodeid = item.find('nodeid').text
                return nodeid  # Return the nodeid of the station with the exact name
        
        # If no exact match is found
        return "정확히 일치하는 정류장을 찾을 수 없습니다."
    else:  
        return "데이터를 받는데 실패했습니다."
    

def get_bus_routes_via_station(city_code, node_id):
    route_list = []
    api_url = 'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getSttnThrghRouteList'
    params = {
        'serviceKey': 'NI9pDLpfb3/7YUQsHOwHKHmy0wHB0LruCc/wJ6Zt+qWR5JPnZdavOjSCJ6bOgpCc0LMAOVQETq4XNYxneKyrEg==',
        'pageNo': 1,
        'numOfRows': 100,  # 최대한 많은 결과를 받기 위해 값 조정
        '_type': 'xml',
        'cityCode': city_code,
        'nodeid': node_id
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # HTTP 요청 오류가 있을 경우 예외를 발생시킵니다.

        soup = BeautifulSoup(response.text, 'xml')
        route_elements = soup.find_all('item')

        for route in route_elements:
            route_info = {}
            for child in route.find_all():
                route_info[child.name] = child.text.strip()
            route_list.append(route_info)

    except Exception as e:
        print(f'버스 노선 조회 중 오류가 발생했습니다: {e}')

    return route_list

city_name = str(input())
route_number = str(input())
city_code, city_type = get_city_code(city_name)
nodenm = str(input())
node_id = get_station_id(city_code, nodenm)

if city_code:
    route_id = get_route_id(city_code, route_number)
    print(f'Route ID: {route_id}, City Code: {city_code}, City Type: {city_type}')
else:
    print('City code could not be retrieved.')

print(get_station_id(city_code, nodenm))


bus_routes = get_bus_routes_via_station(city_code, node_id)

for route in bus_routes:
    print(route)