# 경쟁적 전염

# n*n 크기의 배열
# 바이러스 종류 : 1번 ~ K번
# 1초마다 상,하,좌,우로 증식
# 매초마다 번호가 낮은 종류의 바이러스부터 증식
# 이미 칸에 바이러스가 있다면 증식 불가

# s초 후 (x, y)에 존재하는 바이러스 종류를 출력하기
# 바이러스가 없다면 0 출력
# 왼쪽 위 : (1, 1)

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque([])
# temp = [[0]*n for _ in range(n)] # 증식된 뒤의 배열
virus_list = [] # 바이러스 정보 저장

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] > 0:
            # virus 종류, 시간, i, j
            virus_list.append((arr[i][j], 0, i, j))

# virus 번호가 낮은 것부터 전염시키기 위함
virus_list.sort()
q = deque(virus_list)

s, x, y = map(int, input().split())
delta = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    # virus = (virus 번호, 초, i, j)
    virus = q.popleft()

    if virus[1] == s:
        break

    for d in delta:
        nx, ny = virus[2] + d[0], virus[3] + d[1]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # arr[nx][ny]에 바이러스가 없는 상태라면 바이러스 추가
            if arr[nx][ny] == 0:
                arr[nx][ny] = virus[0]
                q.append((virus[0], virus[1]+1, nx, ny))
                # 바이러스가 낮은 것부터, 시간 순서대로 q에 쌓이게 됨

# 문제에서 (0, 0)은 (1, 1)로 설정
print(arr[x-1][y-1])



# # 바이러스의 위치 찾기
# def find_virus(x, y):
#     virus_list = deque([])
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] > 0:
#                 virus_list.append((i, j, arr[i][j])) # (x, y, 바이러스 종류)
#     return virus_list

# # 바이러스 전염
# def virus(x, y, k):
#     for d in delta:
#         nx = x + d[0]
#         ny = y + d[1]
#         if 0 <= nx and nx < n and 0 <= ny and ny < n:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = k
#                 virus(nx, ny, k)




# def bfs(x, y, sec):
#     virus_list = find_virus(x, y)
#     print(x, y, sec, virus_list)
#     # s초가 지났을 때
#     if sec == s:
#         print(temp[x][y]) # (x, y)위치에 있는 바이러스 종류 출력
#         return
    
#     while virus_list:
#         start = virus_list.pop()
#         print("=====", start)

#         for d in delta:
#             nx, ny = start[0] + d[0], start[1] + d[1]
#             if 0 <= nx and nx < n and 0 <= ny and ny < n:
#                 bfs(nx, ny, sec+1)
#                 # if arr[nx][ny] == 0: # 칸에 바이러스가 퍼지지 않았을 때만
#                 #     arr[nx][ny] = s[2]
#                 # bfs(sec+1)
                    

# bfs(0, 0, 0)
# # print(arr)
