import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
comb = list(combinations_with_replacement(arr, m))
res = []
for i in range(len(comb)):
    temp = [*comb[i]]
    temp.sort()
    if temp in res:
        continue
    res.append(temp)

for r in res:
    print(*r)