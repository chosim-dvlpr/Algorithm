# 0 : 안전영역
# 1 : 벽
# 2 : 바이러스

# m, n : 가로, 세로 크기
# 꼭 3개의 벽을 세워야 함
# 최종 0의 개수 세기

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

# 벽 세우기
for _ in range(n):
  arr.append([1] + list(map(int, input().split())) + [1])
arr = [1]*m + arr + [1]*m

visited = [[0]*m for _ in range(n)] # 방문 표시
q = deque() # 지금까지 온 거리
target = [] # 바이러스가 있는 위치

# 바이러스 위치 확인
for i in range(n):
  for j in range(m):
    if arr[i][j] == 2:
      target.append((i, j))
      if len(target) == 10:
        break

while q:
  for i in range(n):
    for j in range(m):
      if visited[n][m] == 1:
        pass