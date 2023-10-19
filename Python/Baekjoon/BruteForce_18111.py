# 높이를 모두 고르게
# (i, j) 가장 위에 있는 블록을 제거하여 인벤토리에 넣음 : 2초
# 인벤토리에서 블록 하나를 꺼내 (i, j) 가장 위에 있는 블록 위에 놓음 : 1초
# 땅 고르기 작업에 걸리는 최소 시간과 그 경우의 땅의 높이 구하시오
# 땅의 높이는 항상 양수 또는 0

# b : 작업 시작 시 인벤토리에 들어있는 블록
# 땅의 높이는 256 초과할 수 없음

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

mn = 987654321
res = 0
for k in range(257): # 땅 높이 전체 순회
  # 얻은 블록 수, 사용할 블록 수
  use, take = 0, 0
  for i in range(n):
    for j in range(m):
      height = arr[i][j]
      if height > k: # 땅 높이보다 높을 경우
        take += (height - k)
      else:          # 땅 높이보다 낮을 경우
        use += (k - height)
  if b + take < use:
    continue
  else:
    sec = take * 2 + use

  if mn >= sec:
    mn = sec
    if res < k:
      res = k
print(mn, res)