# Baekjoon 1934

import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))
'''
import sys

T = int(sys.stdin.readline())


for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    maxs = max(A, B)

    while maxs != A*B:
        if maxs%A == 0 and maxs%B == 0:
            print(maxs)
            break
        else:
            maxs += 1
            continue
        break
    if maxs == A*B:
        print(A*B)
'''
