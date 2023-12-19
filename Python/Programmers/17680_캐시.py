from collections import deque

def solution(cacheSize, cities):
    total = 0
    stack = deque([])
    
    # 저장소가 0일땐 한번에 곱함
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower() # 대소문자 구분X
        if city not in stack: # 캐시에 저장되어있지 않을 때
            total += 5
            if stack and len(stack) >= cacheSize: # stack에 값이 있는데 꽉 차있을 때
                stack.popleft() # 가장 왼쪽 (가장 오래된 것) 뽑음
            stack.append(city) # 새로 저장
            continue
        # 캐시에 저장된 도시일 때
        stack.remove(city) # 이미 저장된 도시를 빼서 새로 넣어줌
        stack.append(city)
        total += 1
    return total
