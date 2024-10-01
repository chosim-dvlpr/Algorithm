import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
permutation = list(permutations(arr, m))
permutation.sort()
for p in permutation:
    print(*p)