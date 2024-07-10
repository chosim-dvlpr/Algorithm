import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
mx = 0
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for h in range(101):
    visited = [[0]*n for _ in range(n)]
    if mx == n**2:
        print(n**2)
        exit()
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                count += 1
                q = deque([(i, j)])

                while q:
                    (x, y) = q.popleft()
                    visited[x][y] = 1
                    for d in delta:
                        nx = x + d[0]
                        ny = y + d[1]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny] and arr[nx][ny] > h:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
    if count > mx:
        mx = count
print(mx)



