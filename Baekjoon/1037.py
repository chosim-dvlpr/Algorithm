# A는 N의 약수
# N은 A의 배수
# A는 1과 N이 아님
# N의 약수가 주어질 때, N을 구하여라
import sys

n = int(sys.stdin.readline()) # N의 진짜 약수의 개수
n_list = list(map(int, sys.stdin.readline().split())) # N의 진짜 약수 리스트, 2보다 큼

# 선택정렬
def sorting_list(lst, n):
    for i in range(n):
        minidx = i
        for j in range(i+1, n):
            if lst[minidx] > lst[j]:
                minidx = j
        lst[minidx], lst[i] = lst[i], lst[minidx]
    return lst

lst = sorting_list(n_list, n)
if n % 2 == 1: # 홀수일 때
    print((lst[n//2])**2)
else:
    print(lst[0]*lst[-1])