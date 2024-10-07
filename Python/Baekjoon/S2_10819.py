import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
per = permutations(arr)
res = 0

for p in per:
    sums = 0
    for j in range(len(p) - 1):
        sums += abs(p[j] - p[j+1])
    res = max(sums, res)
print(res)
