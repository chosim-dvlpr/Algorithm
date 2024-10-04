import sys
from collections import deque
input = sys.stdin.readline

delta = [(-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2), (-1, -2), (-2, -1)]
INF = 9876543210

for _ in range(int(input())):
    n = int(input())
    curr = list(map(int, input().split()))
    end = list(map(int, input().split()))
    if curr == end:
        print(0)
        continue
    def bfs():
        arr = [[INF] * n for _ in range(n)]

        q = deque()
        q.append([curr[0], curr[1], 0])

        while q:
            x, y, cnt = q.popleft()

            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > cnt+1:
                    arr[nx][ny] = cnt+1
                    q.append([nx, ny, cnt+1])
                if nx == end[0] and ny == end[1]:
                    return arr[nx][ny]                    
        return 0
    print(bfs())