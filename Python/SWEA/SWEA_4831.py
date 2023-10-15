# SWEA 4831

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    station_list = [0] * (N+1)
    M_list = list(map(int, input().split()))

    for num in M_list:
        station_list[num] = 1

    loc = 0
    cnt = 0
    a = True

    while a == True and K+loc < N:
        for i in range(K+loc, loc, -1):
            if station_list[i] == 1:
                loc = i
                cnt += 1
                break
            elif i == loc+1:
                a = False
                cnt = 0

    print(f'#{tc} {cnt}')


