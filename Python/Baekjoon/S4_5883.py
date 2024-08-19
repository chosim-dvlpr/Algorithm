import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arrSet = set(arr)

mx = 1
for a in arrSet:
    cnt = 1
    prev = 0
    for i in range(1, n):
        if arr[i] == a:
            continue
        elif arr[prev] == arr[i]:
            cnt += 1
            if mx < cnt:
                mx = cnt
        else:
            cnt = 1
        prev = i
print(mx)
