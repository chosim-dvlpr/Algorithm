import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lst = list(set(list(permutations(arr, m))))
lst.sort()

for r in lst:
    print(*r)