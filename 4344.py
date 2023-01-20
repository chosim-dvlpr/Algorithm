# baekjoon 4344

import sys

C = int(sys.stdin.readline())

for test_case in range(C):
    std = list(map(int, input().split()))
    avg = sum(std[1:])/std[0]
    sums = 0
    for grade in std[1:]:
        if grade > avg:
            sums += 1
    res = '{:.3f}'.format(round(sums/(len(std)-1), 5)*100)
    print(f'{res}%')
