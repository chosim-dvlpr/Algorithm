# 쉬운 최단거리

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(n)]
start = [0, 0]
# 출발점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start = [i, j]
            arr[i][j] = 0
        elif arr[i][j] == 1:
            arr[i][j] = -1

# # 출발지의 상하좌우는 제외
# exclude = []
# for dx, dy in delta:
#     nx, ny = start[0]+dx, start[1]+dy
#     if 0 <= nx < n and 0 <= ny < m:
#         exclude.append([nx, ny])

# BFS
queue = deque([start])
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while queue:
    [x, y] = queue.popleft()

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == -1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])

for a in arr:
    print(*a)

