# 1~N 자연수 중 M개 선택
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
arr = list(combinations_with_replacement(nums, m))

for a in arr:
    print(*a)