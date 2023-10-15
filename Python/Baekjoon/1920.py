'''
n_lst의 정수 중 m_lst에 있는 정수가 존재하는지 각각 알아내는 프로그램 작성
속도 : set, dictionary >>> list
시간 초과 => n_lst를 set 형태로 변경
'''

import sys

n = int(sys.stdin.readline())
n_lst = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))

for i in m_lst:
    if i in n_lst:
        print(1)
    else:
        print(0)


'''
# 퀵 정렬 & 이진 탐색 => Recursion Error => limit 해제 (sys.setrecursionlimit(10**6))
# => 시간 초과..

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))

def QuickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        QuickSort(a, begin, p-1)
        QuickSort(a, p+1, end)

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

def binsearch(a, n, key):
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:    # 검색 성공
            return 1
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0                    # 검색 실패

QuickSort(n_lst, 0, n-1)    # 정렬

for i in m_lst:
    print(binsearch(n_lst, n, i))
'''