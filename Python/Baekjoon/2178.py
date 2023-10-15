# (1,1) 출발 => (n, m) 도착
# visited 표시가 아닌 0 <= nx < n 등의 범위로 하게 되면 시간 초과

def bfs(x, y, cnt, n, m):
    q = [(x, y, cnt)]
    while q:
        x, y, cnt = q.pop(0)
        for dx, dy in delta:
            nx = x+dx
            ny = y+dy
            if not visited[nx][ny] and nx == n and ny == m:
                return cnt + 1
            elif not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))
                continue


n, m = map(int, input().split())    # n행, m열
arr = [[0] + list(map(int, input())) + [0] for _ in range(n)]
arr = [[0]*(m+2)] + arr + [[0]*(m+2)]
visited = [[False]*(m+2) for _ in range(n+2)]
visited[1][1] = True

delta = [(0,1), (1, 0), (0, -1), (-1, 0)]

print(bfs(1, 1, 1, n, m))
