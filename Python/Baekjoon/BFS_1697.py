 # n, k 위치

# 현재 위치가 x라면
# 1초에 +-1씩 이동
# 순간이동 시 1초에 2*x로 이동
# n이 k로 갈 수 있는 가장 빠른 시간은 몇 초 후?

from collections import deque

n, k = map(int, input().split())
mx = 200000
visited = [0] * (mx+1)

def bfs():
    queue = deque([n])
    while queue:
        q = queue.popleft()
        if q == k:
            print(visited[q])
            return
        for i in (q-1, q+1, q*2):
            if 0 <= i <= mx and not visited[i]:
                visited[i] = visited[q] + 1
                queue.append(i)

bfs()
