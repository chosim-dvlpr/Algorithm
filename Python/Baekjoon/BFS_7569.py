import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

arr = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)
# arr = [
#   [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 
#   [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# ]

queue = deque([]) # (세로, 가로, 높이)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append((j, k, i))

# 모든 토마토가 익어있을 때
if len(queue) == h*m*n:
    print(0)
    exit()
else:
    delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    # 익은 토마토 주변 순회
    while queue:
        q = queue.popleft()
        x = q[0]
        y = q[1]
        z = q[2]
        for d in delta:
            nx, ny, nz = q[0]+d[0], q[1]+d[1], q[2]+d[2]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                queue.append((nx, ny, nz))
    # 토마토가 모두 익지 않은 경우 판별
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    print(-1)
                    exit()
    # 모든 토마토가 익어있을 때
    answer = 0
    for i in range(h):
        for j in range(n):
            # 각 배열의 최댓값을 구함
            answer = max(answer, max(arr[i][j]))
    print(answer-1)
