# n개의 수
# i번째 수부터 j번째 수까지 합을 구하기
# m : 합을 구해야 하는 횟수
# DP?


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0]*n
arr[0] = lst[0]
for i in range(1, n):
    arr[i] = arr[i-1] + lst[i]

for _ in range(m):
    i, j = map(int, input().split())
    # 인덱스로 변경
    i -= 1
    j -= 1
    if i != 0:
        print(arr[j] - arr[i-1])
        continue
    print(arr[j])


