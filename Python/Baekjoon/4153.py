# 내장함수 사용하지 않고 풀기

import sys

a, b, c = 1, 1, 1

while a != 0 and b != 0 and c != 0:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst == [0, 0, 0]:
        break
    maxs = 0
    maxs_idx = -1
    for idx, num in enumerate(lst):
        if num > maxs:
            maxs = num
            maxs_idx = idx
    lst = lst[:maxs_idx] + lst[maxs_idx+1:]
    
    if maxs**2 == lst[0]**2 + lst[1]**2:
        print('right')
    else:
        print('wrong')
        
