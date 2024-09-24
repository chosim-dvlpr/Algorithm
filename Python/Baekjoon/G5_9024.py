import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    start = 0
    end = n-1
    mn = abs(arr[start] + arr[end] - target)
    res = []

    while start < end:
        if target > arr[start] + arr[end]:
            if mn == abs(arr[start] + arr[end] - target):
                res.append((start, end))
            elif mn > abs(arr[start] + arr[end] - target):
                mn = abs(arr[start] + arr[end] - target)
                res = [(start, end)]
            start += 1
        elif target < arr[start] + arr[end]:
            if mn == abs(arr[start] + arr[end] - target):
                res.append((start, end))
            elif mn > abs(arr[start] + arr[end] - target):
                mn = abs(arr[start] + arr[end] - target)
                res = [(start, end)]
            end -= 1
        else:
            if mn == abs(arr[start] + arr[end] - target):
                res.append((start, end))
            else:
                res = [(start, end)]
                mn = 0
            
            end -= 1
            if start < end and abs(arr[start] + arr[end] - target) > mn:
                end += 1
            elif start < end and abs(arr[start] + arr[end] - target) == mn:
                continue
            elif start < end and abs(arr[start] + arr[end] - target) < mn:
                res = [(start, end)]
                mn = abs(arr[start] + arr[end] - target)
                continue
            
            start += 1
            if start < end and abs(arr[start] + arr[end] - target) > mn:
                start -= 1
            elif start < end and abs(arr[start] + arr[end] - target) == mn:
                continue
            elif start < end and abs(arr[start] + arr[end] - target) < mn:
                res = [(start, end)]
                mn = abs(arr[start] + arr[end] - target)
                continue

            start += 1
            end -= 1

    print(len(res))
            



