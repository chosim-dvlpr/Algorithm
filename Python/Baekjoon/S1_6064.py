import sys
input = sys.stdin.readline

tc = int(input())

def check(m, n, x, y):
    res = x
    while res <= m * n:
        if (res - x) % m == 0 and (res - y) % n == 0:
            return res
        res += m
    return -1
    
for _ in range(tc):
    m, n, x, y = map(int, input().split())
    print(check(m, n, x, y))
