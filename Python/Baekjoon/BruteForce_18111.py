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
sums = 0
for a in arr:
  sums += sum(a)

avg = int(sums/n/m)
sec = 0
for i in range(n):
  for j in range(m):
    while arr[i][j] != avg:
      print('실행')
      if arr[i][j] < avg:
        if b != 0:
          sec += 1
          arr[i][j] += 1
          b -= 1
          continue
        else:
          avg -= 1
          continue
      elif arr[i][j] > avg:
        sec += 2
        arr[i][j] -= 1
        b += 1
print(sec, avg)
