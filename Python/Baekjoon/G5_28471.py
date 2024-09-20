import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

delta = [(0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
visited = [[False] * n for _ in range(n)]
res = 0

def bfs(i, j):
    global visited

    visited[i][j] = True
    q = deque()
    q.append((i, j))

    while q:
        (x, y) = q.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))    

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'F':
            bfs(i, j)
            break

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            res += 1

print(res-1)