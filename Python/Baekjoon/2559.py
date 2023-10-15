'''
n : 수열의 개수
k : 연속된 숫자의 개수
k개의 연속된 숫자의 합이 최대가 될 때의 값을 구하기
'''
import sys
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

if k == 1:
    print(max(lst))
else:
    sums = sum(lst[:k])
    temp = [sums]
    for i in range(1, n-k+1):
        sums = sums - lst[i-1] + lst[i+k-1]
        temp.append(sums)
    print(max(temp))