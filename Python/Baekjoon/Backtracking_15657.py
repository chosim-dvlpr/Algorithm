import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
temp = []
res = []

def backtracking(idx, temp):
    if len(temp) == m:
        temp.sort()
        res.append(temp)
        return

    for i in range(idx, n):
        backtracking(i, temp + [lst[i]])


backtracking(0, temp)
res.sort()
for r in res:
    print(*r)