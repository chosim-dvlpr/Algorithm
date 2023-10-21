# n종류의 동전의 가치의 합을 k로 만들기
# 이때 필요한 동전 개수의 최솟값 구하기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []

for _ in range(n):
  lst.append(int(input()))

mn = 987654321
arr = [0]*n

def func(idx, arr, cnt, sums):
  global mn

  if sums > k:
    return
  
  elif sums == k:
    if mn > cnt:
      mn = cnt
    return
  
  else:
    arr[idx] = 1
    for i in range(n):
      if arr[i] == 1:
        sums += lst[i]
    func(idx+1, arr, cnt+1, sums)
    arr[idx] = 0
    func(idx+1, arr, cnt+1, sums)

func(1, )
