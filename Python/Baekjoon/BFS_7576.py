# 토마토가 모두 익을 때까지의 최소 날짜
# 처음부터 모든 토마토가 익어있으면 0 출력
# 모든 토마토가 익지 못하는 상황이면 -1

# 익은 토마토의 좌표를 모두 구함
# 토마토의 좌표를 하나씩 구하면서 bfs

# 방문하지 않은 지역 확인 후 다시 bfs

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 익은 토마토 저장
queue = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

# 모든 토마토가 익어있을 때
if len(queue) == m*n:
    print(0)
    exit()
else:
    # 익은 토마토 확인
    while queue:
        q = queue.popleft()
        x, y = q[0], q[1]
        for d in delta:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                # 배열에 시간을 저장 
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()
    # 배열에 저장된 시간의 최댓값을 구함
    answer = max(answer , max(arr[i]))
print(answer-1)
