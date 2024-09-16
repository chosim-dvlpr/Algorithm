import sys
from collections import deque
input = sys.stdin.readline


while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    arr = []
    for _ in range(m):
        lst = list(map(int, input().split()))
        arr.append(lst)
    
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    q = deque()
    res = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                arr[i][j] = 0
                res += 1
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in delta:
                        nx = x + d[0]
                        ny = y + d[1]
                        if nx < m and nx >= 0 and ny < n and ny >= 0 and arr[nx][ny] == 1:
                            q.append((nx, ny))
                            arr[nx][ny] = 0

    print(res)