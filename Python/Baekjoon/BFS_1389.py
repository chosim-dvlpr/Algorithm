# 케빈 베이커의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
kb = [[0] * (n+1) for _ in range(n+1)] # 케빈 베이커의 수

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    q = deque([i])
    while q:
        start = q.popleft()
        for arr in graph[start]:
            if kb[i][arr] == 0 and i != arr:
                kb[i][arr] += kb[i][start] + 1
                q.append(arr)

mn = 9876543210
answer = 0
for i, k in enumerate(kb):
    sums = sum(k)
    if i != 0 and mn > sums:
        mn = sums
        answer = i
print(answer)
    


