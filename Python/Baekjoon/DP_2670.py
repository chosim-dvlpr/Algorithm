# 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분 찾기
# 그 곱을 출력 (소숫점 셋째자리까지 출력)

import sys
input = sys.stdin.readline

n = int(input())
lst = []
calc = [1] * (10001)

# for _ in range(n):
#     lst.append(int(input()))

calc[1] = float(input().strip())
# calc[2] = calc[1] * float(input())

for i in range(2, n+1):
    # new = float(input())
    calc[i] = round(calc[i-1] * float(input().strip()), 6)
print(calc[:n+1])
