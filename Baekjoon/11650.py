'''
점 n개
x좌표 증가 -> y좌표 증가 순으로 정렬, 출력
'''

import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))
lst.sort(key=lambda x:(x[0], x[1]))
for i in lst:
    print(*i)
