'''
점 N개
y좌표가 증가 -> x좌표 증가하는 순으로 출력
'''
import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))
lst.sort(key=lambda x:(x[1], x[0]))

for x, y in lst:
    print(x, y)
