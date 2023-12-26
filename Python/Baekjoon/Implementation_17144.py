# t초 : 미세먼지 확산 -> 공기청정기 작동 t회 반복


import sys
from collections import deque
input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))

# 공기청정기 위치 확인
for i in range(r): # 공기청정기는 항상 1열에 위치
    if arr[i][0] == -1:
        index = (i, 0)
        break # 공기청정기는 2행을 차지 => 첫행만 저장


# 미세먼지 확산
delta_dust = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dust():
    global arr
    new_arr = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1:
                new_arr[i][j] = -1
            elif arr[i][j] > 0:
                cnt = 0
                for d in delta_dust:
                    nr, nc = i+d[0], j+d[1]
                    if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] > -1:
                        new_arr[nr][nc] += arr[i][j]//5
                        cnt += 1
                new_arr[i][j] += arr[i][j] - (arr[i][j]//5) * cnt
    arr = new_arr



# 공기청정기 작동
# 위쪽 : 반시계
# 아래쪽 : 시계

# 오 -> 아래 -> 왼 -> 위
clock = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 오 -> 위 -> 왼 -> 아래
counter_clock = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def airFlow(delta, start):
    global arr
    prev = deque([0])
    for d in delta:
        start = (start[0]+d[0], start[1]+d[1])
        while 1:
            prev.append(arr[start[0]][start[1]])
            arr[start[0]][start[1]] = prev.popleft()
            if 0 <= start[0]+d[0] < r and 0 <= start[1]+d[1] < c and arr[start[0]+d[0]][start[1]+d[1]] != -1:
                start = (start[0]+d[0], start[1]+d[1])
                continue
            break
        
for _ in range(t):
    dust()
    # 위쪽 (반시계)
    airFlow(counter_clock, (index[0], index[1]))
    # 아래쪽 (시계)
    airFlow(clock, (index[0]+1, index[1]))

cnt = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            cnt += arr[i][j]

print(cnt)