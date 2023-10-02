import sys
from collections import deque

# n : 도시의 개수
# m : 도로의 개수
# k : 거리 정보
# x : 출발 도시의 번호
# lst : 도로 (단방향)

# x부터 출발하여, 최단거리가 k인 도시를 오름차순으로 출력하기
# 최단 거리가 k인 도시가 없으면 -1
# 최단 거리가 k보다 작으면 안됨

n, m, k, x = map(int, sys.stdin.readline().split())
lst = [[]]            # 도로 정보
queue = deque()       # 가지치기 기준점
visited = [0] * (n+1) # 방문 표시
visited[x] = 1        # 출발하는 도시 먼저 방문 표시
answer = []           # 최단 거리가 k인 도시들
cnt = 0               # 거리

for _ in range(m):
  lst.append(list(map(int, sys.stdin.readline().split())))

def bfs():
  global visited, queue, cnt

  if not queue:
    return

  if cnt > k:
    return
    
  s = queue.pop(0) # 가지치기 기준점

  # 인접 확인
  for r in lst[s]:
    # 방문하지 않았다면
    if not visited[r]:
      queue.append(r)
      visited[r] = 1
      cnt += 1
  
  bfs() # queue가 빌 때까지 반복

  # return answer

bfs()
print(cnt)