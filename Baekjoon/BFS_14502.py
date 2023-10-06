# 0 : 안전영역
# 1 : 벽
# 2 : 바이러스

# m, n : 가로, 세로 크기
# 꼭 3개의 벽을 세워야 함
# 최종 0의 개수 세기

import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = deque([]) # 초기 배열
# well = deque([[0]*m for _ in range(n)]) # 벽 세운 뒤의 배열
# well = [[0]*m for _ in range(n)] # 벽 세운 뒤의 배열

# 초기 배열
for _ in range(n):
    arr.append(list(map(int, input().split())))

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 방향
# cnt = 0 # 새로 세운 벽의 개수
result = 0 # 안전지대 개수

def bfs():
    global result

    queue = deque() # 바이러스가 있는 곳의 좌표
    well = copy.deepcopy(arr)
    
    # 바이러스 전파하기
    for i in range(n):
        for j in range(m):
            if well[i][j] == 2:
                queue.append((i, j))
                # virus(i, j)
    # result = max(result, safe_zone())
    # return
    while queue:
        x, y = queue.popleft()

        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if 0 > nx or n <= nx or 0 > ny or m <= ny:
                continue
            if well[nx][ny] == 0:
                well[nx][ny] = 2 # 바이러스 감염
                queue.append((nx, ny)) # 바이러스 위치 좌표 추가
    safe = 0
    for i in range(n):
        safe += well[i].count(0)
    result = max(result, safe)

# 벽 세우기
def add_well(cnt):

    # 종료조건
    if cnt == 3:
        bfs()
        return
    
    # 아직 벽을 세 개 미만 추가했을 때 새로 벽을 세움
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1   # 벽을 세움
                add_well(cnt+1)
                arr[i][j] = 0   # 원 상태로 복귀
                # add_well(cnt)

add_well(0)
print(result)


# # 바이러스 위치 확인
# for i in range(n):
#   for j in range(m):
#     if arr[i][j] == 2:
#       target.append((i, j))
#       if len(target) == 10:
#         break
# i = 0
# while 1:
#     if i == len(target):
#       break

#     visited[target[i][0]][target[i][1]] = 1
#     i += 1
#     curr = [target[i][0], target[i][1]] # 현재 위치

#     for d in delta:
#       nx = curr[0] + d[0]
#       ny = curr[1] + d[1]
#       if 0 < nx < n and 0 < ny < m:
#         if arr[nx][ny] == 0 and visited[nx][ny] == 0: # 길이 있고 방문하지 않았다면
          
      
      
