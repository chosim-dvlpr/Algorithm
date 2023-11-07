# n명의 사람
# 각 사람이 돈을 인출하는데 걸리는 시간 P
# 인원 배열 => 5!
# 누적합 구하기 => 최솟값 찾기
# 누적합이 현재 최솟값보다 크면 종료

# 값이 작은 순으로 순서를 정하기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split())) # 1~n번까지의 값

sums = 0
lst.sort()
for i, d in enumerate(lst):
    sums += (d * (n-i))
print(sums)




# def bfs(chosen, picked):
#     global mn
    
#     if len(chosen) == n:
#         sums = 0
#         for i in range(n):
#             sums += chosen[i] * (i+1)
#         if sums < mn:
#             mn = sums
#         return
#     for i in range(1, n+1):
#         if not picked[i]:
#             chosen.append(p[i])
#             picked[i] = 1
#             bfs(chosen, picked)
#             picked[i] = 0
#             chosen.pop()
# bfs([], picked)
# print(mn)
