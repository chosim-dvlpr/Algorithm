# n장의 카드 중 3장의 카드를 고름
# 카드의 합은 m을 넘지 않으면서 m과 가깝게 만들어야 한다
# 카드의 합을 구하여라

# 부분집합의 합 구하기
# 모든 경우의 수를 다 찾아야 하는 완전탐색 문제
import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(n):
    for j in range(i+1, n):            # i번째 이후 값 확인
        for k in range(j+1, n):        # j번째 이후 값 확인
            sums = num[i] + num[j] + num[k]     # 세 값을 더해 비교
            if sums <= m:
                res = max(res, sums)
print(res)


'''
# 메모리 초과
lst = [[]]

for i in num:
    size = len(lst)
    for j in range(size):
        lst.append(lst[j] + [i])
# print(lst) # [[], [5], [6], [5, 6], [7], [5, 7], [6, 7], [5, 6, 7], [8], [5, 8], [6, 8], [5, 6, 8], [7, 8], [5, 7, 8], [6, 7, 8], [5, 6, 7, 8], [9], [5, 9], [6, 9], [5, 6, 9], [7, 9], [5, 7, 9], [6, 7, 9], [5, 6, 7, 9], [8, 9], [5, 8, 9], [6, 8, 9], [5, 6, 8, 9], [7, 8, 9], [5, 7, 8, 9], [6, 7, 8, 9], [5, 6, 7, 8, 9]]

mx = -1
for i in lst:
    if len(i) == 3:
        a = sum(i)
        if a == m:
            mx = a
        elif a < m:
            mx = max(mx, a)
print(mx)
'''


'''
# 시간 초과
lst = []
for i in range(1<<n):
    sums = 0
    cnt = 0
    for j in range(n):
        if i & (1<<j):
            cnt += 1
            sums += num[j]  # j는 num의 부분집합 중 1이 존재하는 위치를 의미
    if cnt == 3:
        if sums <= m:
            lst.append(sums)
lst.sort()

res = 0

for idx in range(1, len(lst)):
    if lst[idx] == m:
        res = lst[idx]
        break
    elif lst[idx] > m:
        res = lst[idx-1]
        break

print(res)
'''