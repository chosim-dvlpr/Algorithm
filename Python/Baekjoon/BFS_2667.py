# 1 : 집O
# 0 : 집X
# 1이 연결된 곳 = 단지
# 단지 내의 1의 개수 구하기 (오름차순)

import sys
input = sys.stdin.readline


# 값 입력받기
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().strip())))

visited = [[0] * n for _ in range(n)]


delta = [(1,0), (-1,0), (0, 1), (0, -1)]
visited[start[0]][start[1]] = 1

# 백트래킹
def bfs(start, cnt):
    # for i in range(n):
    #     for j in range(n):
    for d in delta:
        nx = start[0] + d[0]
        ny = start[1] + d[1]
        if nx < n and nx >= 0 and ny < n and ny >= 0:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                bfs([nx, ny], cnt+1)
                visited[nx][ny] = 0

# 출력
# 전체 배열 순회
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            start = [i, j]
            bfs(start, 0)
