import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    arr = [0] * (n+1)
    nextNum = 1
    res = 0

    for i in range(1, n+1):
        if arr[i] > 0:
            continue
        res += 1
        nextNum = i
        
        while 1:
            if arr[nextNum] == nextNum:
                break
            arr[nextNum] = nextNum
            nextNum = nums[nextNum]
    print(res)
