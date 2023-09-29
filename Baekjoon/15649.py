import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(_ for _ in range(1, n+1))
arr = []

def solution():
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return

  for i in range(1, n+1):
    if i not in arr:
      arr.append(i)
      solution()
      arr.pop()

solution()