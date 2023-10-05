# 집 n개
# 집의 좌표 : x1~xn
# 공유기 c개
# 한 집에는 공유기 하나만 설치 가능
# 인접한 두 공유기 거리는 가장 크게
# 가장 인접한 두 공유기 사이의 최대 거리 출력

# 이진 탐색 : 찾고자 하는 값이 중간점과 동일하다고 가정하고 탐색을 수행하면 됨
# 정렬된 상태여야 함

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(int(input()))
lst.sort()

start = 1 # 최소 거리
end = lst[-1] - lst[0] # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 두 공유기 사이의 거리
    value = lst[0]
    count = 1
    
    # 앞에서부터 차근차근 공유기 설치
    for i in range(1, n):
        if lst[i] >= value + mid: # value와 두 공유기 사이 거리 합보다 클 때
            value = lst[i] # value 값 업데이트
            count += 1
    
    # c개 이상의 공유기를 설치할 수 있는 경우, 공유기 사이 거리를 증가시켜 순회
    if count >= c:
        start = mid + 1 # 가능한 최소 거리를 가장 인접한 두 공유기 사이 거리 +1로 설정
        result = mid # 현재까지의 최적 결과를 저장
    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)
