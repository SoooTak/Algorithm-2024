import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# 서원대 목민관 GPS
gpslati = 36.62306236451596 
gpslong = 127.48239826990704 

# GPS좌표로 근처 버스정류장 정보 구하기
def get_station_info_from_gps(gps_lati, gps_long) :
    
    # 버스 정류장 정보를 반환하는 값을 저장하는 딕셔너리
    station_info = {
        'node_nm': None,  
        'node_id': None,  
        'node_no': None,
        'city_code': None  
    }
    
    # 사용할 api 주소 2) [좌표기반근접정류소 목록조회]
    api_url = 'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getCrdntPrxmtSttnList'
    # api에 요청할 요청변수(파라미터)
    params = {
        'serviceKey': 'WwUx24zXj59TFZvpPVxkBRIJJe5LllIGnz99n0p/JNGjtRd7jUwhWHY0OXrkIyDfuhi/J5Mbn1eeYIiO4rjE6A==',
        '_type': 'xml',
        'gpsLati' : gps_lati,   # 위도
        'gpsLong' : gps_long    # 경도
    }
    
    try :
        response = requests.get(api_url, params=params) # api 주소에 params 파라미터를 전송, 전송하면 받게되는 응답을 response 변수에 저장
        response.raise_for_status() #HTTP 요청을 보낼 때 에러 발생 시 에러메세지 출력
        
        soup = BeautifulSoup(response.text, 'xml') # soup 변수에 xml 형식으로 응답(response)을 파싱해 저장
        node_id_element = soup.find('nodeid') # soup에서 <nodeid> ~~~ </nodeid>로 된 부분을 추출해 변수에 저장
        node_nm_element = soup.find('nodenm')
        node_no_element = soup.find('nodeno')
        city_code_element = soup.find('citycode')
        
        if node_id_element:
            station_info['node_id'] = node_id_element.text # 추출한 부분이 있을 때 <nodeid>, </nodeid>를 제거한 텍스트 부분만을 추출해 딕셔너리에 저장
        if node_nm_element:
            station_info['node_nm'] = node_nm_element.text
        if node_no_element:
            station_info['node_no'] = node_no_element.text
        if city_code_element:
            station_info['city_code'] = city_code_element.text
        
    except Exception as e:
        print(f'오류가 발생했습니다: {e}')

    return station_info # 최종적으로 gps값을 이용해 가장 가까운 정류장의 id, 이름, 정류장번호, 도시코드가 담긴 딕셔너리 반환

# 도시코드와 정류장 id를 이용해 그 정류장을 지나가는 모든 버스 출력하기
def noseon(city_code, node_id):
    api_url = 'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getSttnThrghRouteList'
    params = {
        'serviceKey': 'WwUx24zXj59TFZvpPVxkBRIJJe5LllIGnz99n0p/JNGjtRd7jUwhWHY0OXrkIyDfuhi/J5Mbn1eeYIiO4rjE6A==',
        '_type': 'xml',
        'cityCode': city_code,
        'nodeid': node_id
    }
    # 정류장을 지나가는 모든 버스가 저장될 리스트 생성
    bus_list = []
    

    try :
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'xml')
        # 정류장을 지나가는 버스 하나의 정보가 item 안에 묶여있으므로 모든 item 묶음을 추출해 저장하기
        items = soup.find_all('item')
        # item 묶음을 for문을 통해 하나씩 살펴보기
        for item in items:
            # 하나의 버스 정보를 저장할 딕셔너리 생성
            bus_info = {
                'route_id': None,  
                'route_no': None,  
                'route_tp': None,
                'endnodenm': None,
                'startnodenm': None
            }
            # < > ~ </ > 부분을 추출해 저장
            route_id_element = item.find('routeid')
            route_no_element = item.find('routeno')
            route_tp_element = item.find('routetp')
            endnodenm_element = item.find('endnodenm')
            startnodenm_element = item.find('startnodenm')

            # < >, </ > 부분을 제거해 딕셔너리에 저장
            if route_id_element:
                bus_info['route_id'] = route_id_element.text
            if route_no_element:
                bus_info['route_no'] = route_no_element.text
            if route_tp_element:
                bus_info['route_tp'] = route_tp_element.text
            if endnodenm_element:
                bus_info['endnodenm'] = endnodenm_element.text
            if startnodenm_element:
                bus_info['startnodenm'] = startnodenm_element.text
            
            # 버스 리스트에 딕셔너리 저장 후 출력
            bus_list.append(bus_info)
            print(bus_info)
        
    except Exception as e:
        print(f'오류가 발생했습니다: {e}')
    
    # 최종적으로 정류장을 지나는 모든 버스 리스트 반환
    return bus_list

station_info = get_station_info_from_gps(gpslati, gpslong)
print(station_info)
noseon(station_info['city_code'], station_info['node_id'])
