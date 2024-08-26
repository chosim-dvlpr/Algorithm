import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(map(int, input().split()))
res = 0

for i in range(1, m-1):
    left = max(graph[:i])
    right = max(graph[i+1:])
    minHeight = min(left, right)

    if graph[i] < minHeight:
        res += minHeight - graph[i]
print(res)