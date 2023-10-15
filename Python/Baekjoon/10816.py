'''
list => 시간 초과 => dict 사용
'''

import sys

n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))
n_lst.sort()

m = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in n_lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')




# 방법 1 - 시간 초과
# for j in lst:
#     i = 0
#     cnt = 0
#     while 1:
#         if n_lst[i] == j:
#             cnt += 1
#             n_lst.pop(i)
#         else:
#             i += 1
#         if i == len(n_lst):
#             break
#     print(cnt, end=' ')

# 방법 2 - 시간 초과
# i = 0
# while 1:
#     cnt = 0
#     for j in n_lst:
#         if lst[i] == j:
#             cnt += 1
#     print(cnt, end=' ')
#     i += 1
#     if i == len(lst):
#         break
