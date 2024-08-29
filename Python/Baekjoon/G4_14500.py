import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


mx = 0
[x, y] = [0, 0]

# DFS
def dfs(x, y, cnt, sums):
    global mx

    if cnt == 3:
        mx = max(mx, sums)
        # print('mx 업데이트 : ', mx, 'x, y : ', x, y)
        return

    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if nx < n and nx >= 0 and ny < m and ny >= 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, sums + arr[nx][ny])
            visited[nx][ny] = False

# ㅗ 모양 테트리스
tmp = [0, 0]
def dfs2(x, y, cnt, sums):
    global mx, tmp
    if cnt == 3:
        mx = max(mx, sums)
        return
    
    elif cnt == 1:
        tmp = [x, y] # tmp 저장
    
    elif cnt == 2:
        [x, y] = tmp
    
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs2(nx, ny, cnt+1, sums + arr[nx][ny])
            visited[nx][ny] = False




for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, arr[i][j])
        dfs2(i, j, 0, arr[i][j])
        visited[i][j] = False

print(mx)
    
    
    
        
        