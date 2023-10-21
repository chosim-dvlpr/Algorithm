# S : 집합

import sys
from collections import deque

input = sys.stdin.readline

m = int(input())
S = deque([])

for _ in range(m):
  lst = list(map(str, input().split()))
  calc = lst[0]
  
  if calc == "add":
    if int(lst[1]) not in S:
      S.append(int(lst[1]))
  elif calc == "remove":
    if int(lst[1]) in S:
      S.remove(int(lst[1]))
  elif calc == "check":
    if int(lst[1]) in S:
      print(1)
    else:
      print(0)
  elif calc == "toggle":
    if int(lst[1]) in S:
      S.remove(int(lst[1]))
    else:
      S.append(int(lst[1]))
  elif calc == "all":
    S = [i for i in range(1, 21)]
  else:
    S = []
