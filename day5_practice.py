import json

print("--- 1. 딕셔너리(Dictionary) 실습 ---")
# API에서 받아온 '사용자 정보'를 가정
user_data = {
    "id": 101,
    "name": "Alice",
    "email": "alice@example.com",
    "features": ["Chat", "Search", "Translation"]
}

# 1-1. 데이터 접근 (Accessing): 'name' 키로 'Alice' 값을 찾아오기
user_name = user_data["name"]
print(f"사용자 이름: {user_name}")

# 1-2. 데이터 추가 (Adding): 'city' 키와 'Seoul' 값을 추가하기
user_data["city"] = "Seoul"
print(f"도시 추가 후: {user_data}")

# 1-3. 중첩된 데이터 접근: 'features' 리스트의 첫 번째 항목('Chat') 접근하기
first_feature = user_data["features"][0]
print(f"첫 번째 기능: {first_feature}")


print("\n--- 2. 리스트(List) 실습 ---")
# 에이전트의 '채팅 기록'을 가정 (딕셔너리들의 리스트)
chat_history = [
    {"role": "user", "content": "안녕, 오늘 날씨 어때?"},
    {"role": "assistant", "content": "어느 도시 날씨를 알려드릴까요?"}
]

# 2-1. 데이터 추가 (Appending): 사용자의 새 메시지 추가
new_message = {"role": "user", "content": "서울 날씨 알려줘"}
chat_history.append(new_message)
print(f"채팅 기록 추가 후: {chat_history}")

# 2-2. 마지막 데이터 접근: 리스트의 맨 마지막 항목(방금 추가한 메시지) 접근
last_message = chat_history[-1]
print(f"마지막 메시지: {last_message}")


print("\n--- 3. JSON 변환 실습 ---")
# API가 응답한 '텍스트(String)' 형태의 JSON을 가정
json_string = '{"product_id": 1234, "items": ["CPU", "GPU"], "stock": true}'

# 3-1. JSON String -> Python Dictionary (Parsing)
# json.loads() : 문자열(String)을 딕셔너리로 변환
product_dict = json.loads(json_string)
print(f"JSON -> Dict: {product_dict}")

# 3-2. 딕셔너리에서 데이터 접근
product_name = product_dict["items"][1] # 'GPU'
print(f"두 번째 아이템: {product_name}")

# 3-3. Python Dictionary -> JSON String (Dumping)
# json.dumps() : 딕셔너리를 (API로 전송하기 좋은) 문자열로 변환
# indent=2는 예쁘게 출력하기 위한 옵션
json_output = json.dumps(product_dict, indent=2)
print(f"Dict -> JSON:\n{json_output}")