import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    A_h, A_m, B_h, B_m = map(int, input().split())
    A_h += B_h
    A_m += B_m

    if A_m >= 60:
        A_h += 1
        A_m -= 60

    if A_h > 12:
        A_h -= 12

    print(f'#{tc+1} {A_h} {A_m}')
