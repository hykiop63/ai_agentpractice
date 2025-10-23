import requests
import json

print("--- API GET 요청 실습 ---")

# 1. 호출할 API 주소
url = "https://jsonplaceholder.typicode.com/posts/1"

# 2. requests 라이브러리로 GET 요청 보내기
# response 변수에는 API 서버의 모든 응답(상태, 내용 등)이 담깁니다.
response = requests.get(url)

# 3. 응답 상태 확인 (Status Code)
# 200: 성공 (OK)
# 404: 찾을 수 없음 (Not Found)
# 500: 서버 내부 오류
print(f"응답 상태 코드: {response.status_code}")

# 4. 응답 내용(Content) 확인
if response.status_code == 200:
    # 4-1. 응답을 텍스트(String)로 받기
    # print(f"응답 (텍스트): {response.text}")
    
    # 4-2. 응답을 JSON(딕셔너리)으로 자동 변환하여 받기 (가장 많이 사용!)
    # .json()은 Day 5에서 배운 json.loads(response.text)와 유사하게 작동합니다.
    data = response.json()
    
    print(f"응답 (JSON -> Dict): {data}")
    
    # 5. Day 5에서 배운 딕셔너리 접근 실습
    title = data['title']
    print(f"\n게시물 제목: {title}")
    
else:
    print(f"API 호출에 실패했습니다: {response.status_code}")