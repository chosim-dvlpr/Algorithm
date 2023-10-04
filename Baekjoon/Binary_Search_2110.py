# 집 n개
# 집의 좌표 : x1~xn
# 공유기 c개
# 한 집에는 공유기 하나만 설치 가능
# 인접한 두 공유기 거리는 가장 크게
# 가장 인접한 두 공유기 사이의 최대 거리 출력

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = []

for _ in range(n):
    # lst.append(input().replace('\n', ''))
    lst.append(int(input()))

