# Baekjoon 1059
# n을 포함하는 좋은 구간의 개수를 구하여라
# 좋은 구간 == a<b일때, a<=x<=b를 만족하는 모든 정수 x가 s에 포함되지 않음
# n을 포함하는 좋은구간의 개수는?

# # 선택 정렬
# def sorting_list(lst, n):
#     for i in range(n-1):
#         minidx = i
#         for j in range(i+1, n):
#             if lst[minidx] > lst[j]:
#                 minidx = j
#         lst[minidx], lst[i] = lst[i], lst[minidx]
#     return lst

# 인덱스 번호 찾기
# def idx_num(lst, n):
#     for i in range(len(lst)):
#         if lst[i] > n:
#             return i

# 부분집합 생성
# lst = []
# for i in range(1<<len(new_list)):
#     sums_list = []
#     for j in range(len(new_list)):
#         if i & (1<<j):
#             sums_list.append(new_list[j])
#     if len(sums_list) == 2:
#         lst += [sums_list]
# print(lst) # [[2, 3], [2, 4], [3, 4], [2, 5], [3, 5], [4, 5], [2, 6], [3, 6], [4, 6], [5, 6]]

import sys

L = int(sys.stdin.readline()) # L : 집합 s의 크기
s_list = list(map(int, sys.stdin.readline().split())) # s집합에 포함된 정수
n = int(sys.stdin.readline())

s_list.sort()

if n in s_list:
    print(0)
else:
    mins = 0
    maxs = 0

    for i in range(len(s_list)): # 배열 중 n과 근접한 두 수를 구함
        if s_list[i] < n:
            mins = s_list[i]
        if s_list[i] > n:
            maxs = s_list[i]
            break
    mins += 1
    maxs -= 1

    res = (n-mins) * (maxs-n+1) + (maxs-n) # (2-2) * (6-2+1) + (6-2) = 4
    print(res)
