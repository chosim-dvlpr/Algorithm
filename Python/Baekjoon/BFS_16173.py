# 정사각형
# (0, 0) 출발
# 오른쪽, 아래로 이동 가능
# (n-1, n-1) 도착 시 승리
# 현재 밟고있는 칸의 값만큼 이동 가능 (미만, 초과 불가)
# 최종값인 -1값에 도달할 수 있으면 HaruHaru 출력
# 도달할 수 없으면 Hing 출력

import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

res = "res : "
delta = [(0, 1), (1, 0)]
x, y = 0, 0

def bfs(x, y):
  global res

  if arr[x][y] == -1:
    res = "HaruHaru"
    # print(res)
    return 
  
  for d in delta:
    nx, ny = x+d[0]*arr[x][y], y+d[1]*arr[x][y]
    # print(nx, ny)
    if 0 <= nx and nx < n and 0 <= ny and n > ny:
      # print('조건충족', res)
      bfs(nx, ny)
      if res == "HaruHaru":
        break
      
    else: # 실패
      # print('실패', res)
      res = "Hing"
      return

bfs(0, 0)
print(res)