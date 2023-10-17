# 연결되어 있는 곳은 모두 바이러스에 감염
# 바이러스 감염 수 구하기

import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
node = int(input()) # 연결선 수
graph = [[] for _ in range(n+1)] # 노드
visited = [0]*(n+1) # 개수 셌는지 확인
visited[1] = 1

for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
print(graph)
def bfs(idx):
    global cnt

    if idx == node+1:
        print("종료")
        return

    for e in graph[idx]:
        print("idx: ", idx, "e :", e)
        if not visited[e]:
            cnt += 1
            visited[e] = 1
            print('not visited')
            print()
            bfs(idx+1)

bfs(1)
print(cnt)