import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def bfs(idx):
    visited[idx] = 1
    q = deque()
    q.append(idx)
    while q:
        index = q.pop()
        for i in graph[index]:
            if not visited[i]:
                visited[i] = 1
                q.append(i) # bfs는 여기서 q를 반복함
                

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = 1
        cnt += 1
        bfs(i)

print(cnt)