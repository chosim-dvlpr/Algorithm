# 1부터 N까지 자연수 중에서 M개를 고른 수열 구하기

import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(_ for _ in range(1, n+1))
arr = []

def solution():
  if len(arr) == m:
    print(*arr)
    return

  for i in lst:
    arr.append(i)
    solution()
    arr.pop()

solution()