import sys
input = sys.stdin.readline

# 풀이 [1] : 이진탐색 사용
n = int(input())
lst = list(map(int, input().split()))
data = sorted(list(set(lst)))

def bin_search(target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_val = data[mid]
        if mid_val == target:
            return mid
        if mid_val < target:
            start = mid + 1
            continue
        end = mid - 1
    return -1

for i in lst:
    print(bin_search(i), end=' ')

# 풀이 [2] : dict 사용
n = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(list(set(lst)))
dic = {sorted_lst[i] : i for i in range(len(sorted_lst))} # 정렬한 인덱스 번호 저장 == 나보다 작은 원소의 수
for i in lst:
    print(dic[i], end=' ')