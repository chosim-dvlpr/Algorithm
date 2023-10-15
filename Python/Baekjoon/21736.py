
# from collections import deque

def bfs(x, y):
    cnt = 0
    # q = deque()
    q = []
    visited[x][y] = 1
    q.append((x, y))

    while q:
        # x, y = q.popleft()
        x, y = q.pop(0)
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if arr[nx][ny] != 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    if arr[nx][ny] == 'P':
                        cnt += 1
    return cnt

n, m = map(int, input().split())

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            cnt = bfs(i, j)
            break
if cnt == 0:
    cnt = 'TT'

print(cnt)