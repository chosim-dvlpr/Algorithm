import sys
from collections import deque
input = sys.stdin.readline

# 0 : 하얀색
# 1 : 파란색
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
delta = [(0, 1), (1, 0)]
visited = [[0]*n for _ in range(n)]

def bfs(x, y, num):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in delta:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = 1

white = 0
blue = 0
# visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 0:
            print('0 : ', i, j)
            bfs(i, j, 0)
            white += 1
        if not visited[i][j] and arr[i][j] == 1:
            print('1 : ', i, j)
            bfs(i, j, 0)
            blue += 1

print(white)
print(blue)
                
        