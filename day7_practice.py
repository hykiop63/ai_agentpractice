import requests
import json
from pprint import pprint # 데이터를 깔끔하게 출력하기 위한 라이브러리 (선택 사항)

print("--- 실전: 날씨 API 호출 및 데이터 가공 (Day 7) ---")

# 1. API 기본 주소 open-meteo free api data site
base_url = "https://api.open-meteo.com/v1/forecast"

# 2. 쿼리 파라미터 설정 (Day 5: 딕셔너리 활용)
# requests는 이 딕셔너리를 URL 뒤에 '?key=value&...' 형태로 변환해줍니다.
params = {
    "latitude": 37.5665,     # 서울 위도
    "longitude": 126.9780,    # 서울 경도
    "current_weather": True,   # 현재 날씨 정보를 요청하는 옵션
    "timezone": "auto"         # 시간대 자동 설정 옵션 추가
}
print(f"요청 조건(Params): {params}")

# 3. API 호출
try:
    # requests.get(url, params=딕셔너리) 형식으로 요청합니다.
    response = requests.get(base_url, params=params)
    
    # 3-1. 응답 상태 코드가 200이 아니면 예외(Exception)를 발생시킵니다.
    response.raise_for_status() 
    
    data = response.json()
    
    # 4. 필요한 데이터만 추출 (Day 5: 중첩된 딕셔너리 접근)
    
    # data 딕셔너리 안의 'current_weather' 키에 접근
    current_weather = data['current_weather']
    
    # current_weather 딕셔너리 안의 'temperature' 및 'windspeed' 키에 접근
    temperature = current_weather['temperature']
    windspeed = current_weather['windspeed']
    
    print("\n--- 서울 현재 날씨 정보 추출 성공 ---")
    print(f"API 호출 URL: {response.url}")
    print(f"기온: {temperature} °C")
    print(f"풍속: {windspeed} km/h")
    
    # (선택 사항) 전체 데이터 구조를 확인하려면 주석 해제:
    print("\n--- 전체 응답 데이터 구조 ---")
    pprint(data) 

except requests.exceptions.HTTPError as errh:
    # 400대 또는 500대 상태 코드가 발생했을 때 잡는 예외
    print(f"HTTP 오류 발생: API 요청이나 서버에 문제가 있습니다. {errh}")
except requests.exceptions.RequestException as err:
    # 인터넷 연결 끊김 등 요청 자체에 문제가 있을 때 잡는 예외
    print(f"요청 중 오류 발생 (인터넷 연결을 확인하세요): {err}")