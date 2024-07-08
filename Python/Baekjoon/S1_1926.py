import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 그림의 개수
# 가장 넓은 그림의 크기 출력 (없다면 0)

q = deque([])
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
res = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
            count = 1

            while q:
                (x, y) = q.popleft()
                arr[x][y] = 0
                for d in delta:
                    nx = x + d[0]
                    ny = y + d[1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 1:
                        arr[nx][ny] = 0
                        q.append((nx, ny))
                        count += 1
            res.append(count)

if len(res) == 0:
    print(0)
    print(0)
else:
    print(len(res))                        
    print(max(res))


