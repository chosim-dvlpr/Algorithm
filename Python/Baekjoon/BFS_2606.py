# 연결되어 있는 곳은 모두 바이러스에 감염
# 바이러스 감염 수 구하기

import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
node = int(input()) # 연결선 수
graph = [[] for _ in range(n+1)] # 노드
visited = [0]*(n+1) # 개수 셌는지 확인

for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def bfs(idx):
    for e in graph[idx]:
        if not visited[e]:
            cnt += 1
        


for i, g in enumerate(graph):
    pass
