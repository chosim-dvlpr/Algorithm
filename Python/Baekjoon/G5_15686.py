# 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합

# 1 : 집
# 2 : 치킨집

# 도시의 치킨 거리의 최솟값 출력
# 치킨집이 많아야 치킨 거리가 최소가 됨

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
two = []
one = []

# 2 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            two.append((i, j))
        elif arr[i][j] == 1:
            one.append((i, j))

# 조합 (순서 상관x)
twoCombList = list(combinations(two, m))

sums_min = [9875543210, ()]
for comb in twoCombList:
    sums = 0
    for x, y in one:
        mn = 9876543210  
        for cx, cy in comb:
            mn = min(abs(x-cx) + abs(y-cy), mn)
        sums += mn
    if sums < sums_min[0]:
        sums_min = [sums, comb]
print(sums_min[0])
