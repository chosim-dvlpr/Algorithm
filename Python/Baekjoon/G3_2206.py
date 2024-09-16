# 1 : 벽
# (1, 1) -> (n, m) 으로 이동, 최단 경로
# 한 개의 벽을 부수고 이동하는 것이 더 짧아진다면 1번까지 부수고 이동해도 됨
# 상하좌우
# 최단경로 구하기
# 안되면 -1

# 벽 부수는 상황
# 1. 갈 방향이 모두 막혔을 때
# - 뚫고 다시 원상복구
# brokeCount = 1

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().strip()))
    arr.append(a)

curr = (0, 0, 1, 1) # x, y, brokeCount, 거리
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()
q.append(curr)
visited = [[[False, False] for _ in range(m)] for _ in range(n)] # 방문 여부 - [벽 부술 수 있는 횟수가 0번일 때, 1번 있을 때]
visited[curr[0]][curr[1]][1] = True # 방문 표시

while q:
    x, y, brokeCnt, res = q.popleft()
    
    if x == n-1 and y == m-1:
        print(res)
        exit()
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != 1 and not visited[nx][ny][brokeCnt]:
                q.append((nx, ny, brokeCnt, res+1))
                visited[nx][ny][brokeCnt] = True
            elif arr[nx][ny] == 1 and brokeCnt == 1 and not visited[nx][ny][0]:
                q.append((nx, ny, 0, res+1))
                visited[nx][ny][0] = True
                
print(-1)