import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

def solution(n, m):
  lst = list(_ for _ in range(1, n+1))

  print("lst : ", lst)

  for i in range(1, n+1):
    for j in range(1, 1<<i):
      print(i, j)


  # if m != 1:
  #   arr = list(combinations(lst, m))
    
  #   for a in arr:
  #     print(''.join(str(a)))
  #   all_lst = list(a for a in arr)
  # return all_lst
print(solution(n, m))