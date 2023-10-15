import sys
from collections import deque

# n : 도시의 개수
# m : 도로의 개수
# k : 거리 정보
# x : 출발 도시의 번호
# graph : 도로 (단방향)

# x부터 출발하여, 최단거리가 k인 도시를 오름차순으로 출력하기
# 최단 거리가 k인 도시가 없으면 -1
# 최단 거리가 k보다 작으면 안됨

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)] # 도로 정보
distance = [-1] * (n+1) # 도시들의 최단거리 정보
distance[x] = 0 # 자기 자신으로 가는 거리는 0
queue = deque([x])    # 가지치기 기준점

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)

while queue: # queue에 값이 없을 때까지 반복
  curr = queue.popleft() # 현재 위치

  for next in graph[curr]: # 현재 위치에서 갈 수 있는 정점 순회
    if distance[next] == -1: # 다음 위치를 방문하지 않았다면
      distance[next] = distance[curr] + 1 # 다음 위치까지 도달했을 때의 거리 정보 저장
      queue.append(next) # 다음 위치 정보 저장

if k in distance:
  for i in range(1, n+1):
    if distance[i] == k:
      print(i)
else:
  print(-1)