'''
땅 고르기
가로 M, 세로 N
B : 인벤토리에 있는 수

(i, j)의 높이 -1 => 인벤토리 +1 : 2초
인벤토리 -1 => (i, j)의 높이 +1 : 1초

땅의 높이 : 0 이상

땅을 평평하게 고르는데 걸리는 최소시간과 땅의 높이를 출력하기
- 답이 여러개 있다면 땅의 높이가 가장 높은 것을 출력
'''

import sys

n, m, b = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
