import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
INF = 1e9

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

mx = 0

for i in range(1, n+1):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, i)) # 거리합계, 현재 노드
    distance[i] = 0

    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] >= dist:
            for nxt, next_dist in graph[curr]:
                cost = dist + next_dist
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
    temp = 0
    for i, dist in enumerate(distance):
        if dist <= m:
            temp += arr[i]
    mx = max(temp, mx)
print(mx)
