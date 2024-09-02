import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort() # [2, 3, 5, 5, 9]
mn = 10e9

for i in range(n-3):
    for j in range(i+3, n):
        standard = arr[i] + arr[j] # 기준점
        # 비교 대상
        s, e = i+1, j-1
        while s < e:
            sums = arr[s] + arr[e]
            # print(sums)
            mn = min(mn, abs(standard - sums))
            if sums < standard:
                s += 1
            elif sums > standard:
                e -= 1
            else:
                print(0)
                exit()

print(mn)
