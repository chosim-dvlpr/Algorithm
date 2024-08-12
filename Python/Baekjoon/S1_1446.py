import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)
cost = 0

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    s, e, r = map(int, input().split())
    if e > d:
        continue
    graph[s].append((e, r))

q = []
start = 0
heappush(q, (0, start))

while q:
    dist, curr = heappop(q)

    if dist > distance[start]:
        continue

    for e, c in graph[curr]:
        cost = dist + c
        if cost < distance[e]:
            distance[e] = cost
            heappush(q, (cost, e))

print(distance[d])