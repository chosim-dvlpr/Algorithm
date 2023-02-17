# 1929 - 시간초과 방지! - 에라토스테네스의 체 (소수 구하기)
# 먼저 2의 배수 제거
# n**2의 제곱근 = n
# n**2의 제곱근 n보다 작은 수들로 나눠지면 제거

import sys

M, N = map(int, sys.stdin.readline().split())

for num in range(M, N+1):
    if num == 1:
        continue
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            break
    else:
        print(num)
