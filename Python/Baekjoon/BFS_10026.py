import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = [list(input().strip()) for _ in range(n)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque()

# 같은 문자를 확인
def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in delta:
            nx, ny = x + d[0], y + d[1]
            # 같은 구역일 때만 방문
            if 0 <= nx < n and 0 <= ny < n and lst[x][y] == lst[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1


# 적록색약 아닌 경우
visited = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

# 적록색약인 경우
# R를 G로 칠함
for i in range(n):
    for j in range(n):
        if lst[i][j] == 'R':
            lst[i][j] = 'G'

visited = [[0]*n for _ in range(n)]
cnt_blind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt_blind += 1

print(cnt, cnt_blind)
