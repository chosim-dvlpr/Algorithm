import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if queue:
            print(-heappop(queue))
        else:
            print(0)
        continue
    heappush(queue, -x)
