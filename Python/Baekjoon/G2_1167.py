import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)] # (연결된 간선 번호, 거리)

for _ in range(n):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if i%2 == 0 or i == 0 or arr[i] == -1:
            continue
        graph[arr[0]].append((arr[i], arr[i+1]))
        graph[arr[i]].append((arr[0], arr[i+1]))

for i in range(len(graph)):
    graph[i].sort(reverse=True)

def find_farthest_node(start):
    q = deque()
    q.append(start)
    distances = [-1] * (n+1)
    distances[start] = 0
    mx = 0
    farthest_node = 0

    while q:
        node = q.popleft()
        for next_node, dist in graph[node]:
            if distances[next_node] == -1:
                q.append(next_node)
                distances[next_node] = dist + distances[node]
                if mx < distances[next_node]:
                    mx = distances[next_node]
                    farthest_node = next_node
    return mx, farthest_node

max_dist1, farthest_node1 = find_farthest_node(1)
res, _ = find_farthest_node(farthest_node1)
print(res)
