import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
data = sorted(list(set(lst)))

def bin_search(target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_val = data[mid]
        if mid_val == target:
            return mid
        if mid_val < target:
            start = mid + 1
            continue
        end = mid - 1
    return -1

for i in lst:
    print(bin_search(i), end=' ')
