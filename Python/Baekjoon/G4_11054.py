import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
reversed_arr = arr[::-1]

increased = [1 for _ in range(n)]
decreased = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increased[i] = max(increased[i], increased[j]+1)
        if reversed_arr[i] > reversed_arr[j]:
            decreased[i] = max(decreased[i], decreased[j]+1)

mx = 0

for i in range(n):
    mx = max(mx, increased[i] + decreased[n-1-i] - 1)
print(mx)


# idxs = [i for i in range(n)]

# def left(comb, idx):
#     start = 0
#     end = idx-1
#     if idx == 0:
#         return True
#     for i in range(start, end):
#         if comb[i] > comb[i+1]:
#             return False
#     return True

# def right(comb, idx):
#     start = idx+1
#     end = len(comb)-1
#     if idx == len(comb)-1:
#         return True
#     for i in range(start, end):
#         if comb[i] < comb[i+1]:
#             return False
#     return True
#     # mid = (start + end) // 2
#     # while start < end:
#     #     if 

# for i in range(n, 0, -1):
#     comb_arr = list(combinations(arr, i))
#     for comb in comb_arr:
#         target = max([*comb])
#         if comb.count(target) >= 2:
#             continue
#         target_idx = comb.index(target)
#         if left(comb, target_idx) and right(comb, target_idx):
#             print(len(comb))
#             exit()
