import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

increased = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increased[i] = max(increased[i], increased[j]+1)
print(max(increased))
