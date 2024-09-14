# R : 순서를 뒤집음
# D : 첫번째 수 버리기 (비어있는데 사용하면 에러)
# 배열 개수보다 D 개수가 더 크면 error

import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    func = input().strip()
    n = int(input())
    arrInput = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arrInput[1:-1].split(',')))
    
    reverse_flag = False
    error_flag = False

    for f in func:
        if f == 'R':
            reverse_flag = not reverse_flag
        elif f == 'D':
            if arr:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error_flag = True
                break
    if error_flag:
        print('error')
    else:
        if reverse_flag:
            arr.reverse()
        print(f'[{",".join(map(str, arr))}]')