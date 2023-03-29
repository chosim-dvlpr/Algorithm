import sys
sys.stdin = open('input.txt')

'''
n//2번째 원소, 오른쪽 원소가 먼저 복사되는 경우의 수 출력
(두 개로 나눴을 때, 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 출력)
'''

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    res = []    # 결과를 저장할 리스트

    i = j = 0

    if left[-1] > right[-1]:    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우
        cnt += 1
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:         # 오른쪽이 더 클 때
                res.append(left[i])         # 왼쪽을 먼저 저장
                i += 1
            else:                           # 왼쪽이 더 클 때
                res.append(right[j])        # 오른쪽을 먼저 저장
                j += 1
        elif len(left) > i:         # 오른쪽은 다 소진한 경우 왼쪽만 res에 저장
            res.append(left[i])
            i += 1
        elif len(right) > 0:        # 왼쪽은 다 소진한 경우 오른쪽만 res에 저장
            res.append(right[j])
            j += 1
    return res


for tc in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(lst)[n//2]
    print(f'#{tc} {res} {cnt}')
