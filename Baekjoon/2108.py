'''
n :홀수
산술평균(means) : n개의 수를 n으로 나눔 -정수형으로 출력 (첫째 자리에서 반올림)
- lst합계 필요
중앙값(median) : n개의 수를 증가하는 순서로 나열 시 중앙에 위치하는 값 (idx = len(lst)//2)
-정렬
최빈값(mode) : n개의 수 중 가장 많이 나타나는 값 -여러개 있다면 두 번째로 작은 값 출력
-정렬?
- [0] * (n+1) list
범위(rng) : n개의 수 중 최댓값과 최솟값의 차이
-정렬
'''

import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)

# 퀵 정렬
def Quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        Quicksort(a, begin, p-1)
        Quicksort(a, p+1, end)

def partition(a, begin, end):
    pivot = (begin + end) // 2
    l = begin
    r = end
    while l < r:
        while l<r and a[l] < a[pivot]:
            l += 1
        while l<r and a[r] >= a[pivot]:
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            a[l], a[r] = a[r], a[l]
    a[pivot], a[r] = a[r], a[pivot]
    return r

Quicksort(lst, 0, len(lst)-1)


# 산술 평균
means = round(sum(lst) / n) # 산술평균 - int로 할 경우 올림이 되어 -1.8이 -1로 출력됨
                            # => round 사용하여 반올림

# 중앙값
median = lst[len(lst)//2]


# 최빈값
mode_list = Counter(lst).most_common(2)
# [(-2, 1), (1, 1)]
# (값, 등장횟수) 리스트로 2개까지 출력, 등장 횟수 많은 순서로 정렬됨
mode = mode_list[0][0]
if len(mode_list) > 1:
    if mode_list[0][1] == mode_list[1][1]:
        mode = mode_list[1][0]


# 범위 구하기
rng = lst[-1] - lst[0]



print(means)
print(median)
print(mode)
print(rng)