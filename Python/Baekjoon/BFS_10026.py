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
# n = int(input())
# lst = [list(map(str, input().strip())) for _ in range(n)]
# arr = [[0]*n for _ in range(n)]
# arr_blind = [[0]*n for _ in range(n)]
# delta = [(0, 1), (1, 0)]

# start = (0, 0)
# queue = deque([start])
# # value = 1
# # value_blind = 1
# arr[start[0]][start[1]] = 1
# arr_blind[start[0]][start[1]] = 1


# while queue:
#     x, y = queue.popleft()
#     for d in delta:
#         nx, ny = x + d[0], y + d[1]
#         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#             queue.append((nx, ny))
#             visited[nx][ny] = 1
            
            # # B일 때
            # if lst[x][y] == color[2]:
            #     if lst[x][y] != lst[nx][ny]:
            #         arr[nx][ny] = value + 1
            #         arr_blind[nx][ny] = value_blind + 1
            #         value, value_blind = value+1, value_blind+1
            #         continue
            #     arr[nx][ny] = arr[x][y]
            #     arr_blind[nx][ny] = arr_blind[x][y]
            #     continue
            # # G일 때
            # elif lst[x][y] == color[1]:
            #     # G - B
            #     if lst[nx][ny] == color[2]:
            #         arr[nx][ny] = value + 1
            #         arr_blind[nx][ny] = value_blind + 1
            #         value, value_blind = value+1, value_blind+1
            #         continue
            #     # G - R
            #     elif lst[nx][ny] == color[0]:
            #         arr[nx][ny] = value + 1
            #         arr_blind[nx][ny] = value_blind
            #         value, value_blind = value+1, value_blind
            #         continue
            #     # G - G
            #     arr[nx][ny] = arr[x][y]
            #     arr_blind[nx][ny] = arr_blind[x][y]
            #     continue
            # # R일 때
            # # R - B
            # if lst[nx][ny] == color[2]:
            #     arr[nx][ny] = value + 1
            #     arr_blind[nx][ny] = value_blind + 1
            #     value, value_blind = value+1, value_blind+1
            #     continue
            # # R - G
            # elif lst[nx][ny] == color[1]:
            #     arr[nx][ny] = value + 1
            #     arr_blind[nx][ny] = value_blind
            #     value, value_blind = value+1, value_blind
            #     continue
            # arr[nx][ny] = arr[x][y]
            # arr_blind[nx][ny] = arr_blind[x][y]
            # continue
# mx = 0
# mx_blind = 0
# for a in arr:
#     mx = max(mx, max(a))
# for a in arr_blind:
#     mx_blind = max(mx_blind, max(a))
# print(arr)
# print(arr_blind)
# print(mx, mx_blind)

