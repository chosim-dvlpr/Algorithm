# 1 구역의 개수 찾기 

import sys
from collections import deque
input = sys.stdin.readline

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 1 좌표 저장 후 delta 순회
def bfs(i, j):
    global arr
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in delta:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                # 방문 시 값을 0으로 바꿈
                arr[nx][ny] = 0
                q.append((nx, ny))


tc = int(input())

for t in range(tc):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)