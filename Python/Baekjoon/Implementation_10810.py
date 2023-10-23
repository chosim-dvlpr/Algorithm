import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0] * (n+1)

for _ in range(m):
  s, e, k = map(int, input().split())
  for i in range(s, e+1):
    lst[i] = k

for i in range(1, n+1):
  print(lst[i], end=" ")