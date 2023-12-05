# DFS와 BFS로 탐색한 결과 출력하기
# 방문할 수 있는 정점이 여러개라면 정점 번호가 더 작은 것 먼저 방문

import sys
from collections import deque
input = sys.stdin.readline

# n : 정점의 개수
# m : 간선의 개수
# v : 탐색 시작 정점 번호
# 간선 : 양방향

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# graph : [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]

# 간선이 여러개라면 작은 노드부터 방문
for g in graph:
    g.sort()

print(v, end=" ")
visited_list = [v]
def dfs(idx, visited_list):
    for i in graph[idx]:
        if i not in visited_list:
            visited_list.append(i)
            print(i, end=" ")
            dfs(i, visited_list)


def bfs(idx):
    visited = [idx]
    q = deque(visited)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if i not in visited:
                q.append(i)
                visited.append(i)
                print(i, end=" ")
    return 

dfs(v, visited_list)
print()
print(v, end=" ")
bfs(v)