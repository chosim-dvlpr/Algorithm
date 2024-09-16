# 노드 : 7개
# 순서 O

# 1 - 6 - 3 - 5
# |
# 4 - 2
# |
# 7

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
root = 1
graph = [[] for _ in range(n+1)]
res = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

q = deque()
q.append(root)

while q:
    curr = q.popleft()
    for nxt in graph[curr]:
        if res[nxt] == 0:
            res[nxt] = curr
            q.append(nxt)
for i in range(2, n+1):
    print(res[i])
