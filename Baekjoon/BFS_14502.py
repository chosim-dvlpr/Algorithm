# 0 : 안전영역
# 1 : 벽
# 2 : 바이러스

# m, n : 가로, 세로 크기
# 꼭 3개의 벽을 세워야 함
# 최종 0의 개수 세기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [] # 초기 배열
well = [[0]*m for _ in range(n)] # 벽 세운 뒤의 배열

# 초기 배열
for _ in range(n):
  arr.append(list(map(int, input().split())))

# visited = [[0]*m for _ in range(n)] # 방문 표시
# target = [] # 바이러스가 있는 위치
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 방향
cnt = 0 # 새로 세운 벽의 개수
result = 0 # 안전지대 개수
# curr = [0, 0] # 시작 위치

# 바이러스 전염
def virus(nx, ny):
    for d in delta:
        nx = nx + d[0]
        ny = ny + d[1]
        for i in range(n):
            for j in range(m):
                    if arr[i][j] == 0:
                        arr[i][j] = 2 # 바이러스 감염
                        virus(nx, ny)

# 안전지대 개수 확인
def safe_zone():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                result += 1
    return result

# 벽 세우기
def add_well(cnt):
    global result

    # 종료조건
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    result += 1
                    print("arr[i][j] == 0 : ", result)
        result = max(result, safe_zone())
        print("cnt == 3 : ", result)
    
    # 아직 벽을 세 개 미만 추가했을 때
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                add_well(cnt+1)
                arr[i][j] = 0
                add_well(cnt)

add_well(0)



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
          
      
      
