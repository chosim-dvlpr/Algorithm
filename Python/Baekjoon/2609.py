'''
두 개의 자연수 n, m의 최대공약수와 최소공배수 출력
시간 단축 => 최대공약수는 두 자연수 중 최소값부터 줄여가며 비교
=> 최소공배수는 최대공약수의 배수
'''

import sys

n, m = map(int, sys.stdin.readline().split())
i = min(n, m)+1
k = 1
flag = 0
mn = mx = 0

while 1:
    if mn == 0:
        i -= 1
    else:
        i = mn * k
        k += 1
    if flag == 0 and n%i == 0 and m%i == 0:
        mn = i
        flag = 1
    if flag == 1 and i%n == 0 and i%m == 0:
        mx = i
        break

print(mn)
print(mx)