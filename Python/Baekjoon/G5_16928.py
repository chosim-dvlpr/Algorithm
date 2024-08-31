import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
INF = 10e9
arr = [INF] * 101

ladders = {}
snakes = {}

for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

start = 1
q = deque([[start, 0]])

while q:
    [curr, cnt] = q.popleft()
    if curr > 100:
        break
    upper = ladders.get(curr)
    lower = snakes.get(curr)
    if upper:
        q.append([upper, cnt])
        arr[upper] = min(arr[upper], cnt)
    elif lower:
        q.append([lower, cnt])
        arr[lower] = min(arr[lower], cnt)
    else:
        dice = 6
        while dice > 0:
            if curr + dice > 100:
                dice -= 1
                continue
            if arr[curr + dice] > cnt+1:
                q.append([curr + dice, cnt+1])
                arr[curr + dice] = cnt+1
            dice -= 1

print(arr[100])
