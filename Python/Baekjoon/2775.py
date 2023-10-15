# 아파트 : 0층부터
# 0층 i호 : i명

# 1층 1호 : 0층 1호 = 1명
# 1층 2호 : 0층 1,2호 = 1+2명 = 3 = 1층 1호 + 2
# 1층 3호 : 0층 1,2,3호 = 1+2+3 = 6 = 1층 2호 + 3

# 2층 1호 : 1층 1호 = 1명
# 2층 2호 : 1층 1,2호 = 1+3 = 4 = 2층 1호 + 3
# 2층 3호 : 1층 1,2,3호 = 1+3+6 = 10 = 2층 2호 + 6

# 3층 1호 : 1명
# 3층 2호 : 2층 1,2호 = 1 + 4 = 5 = 3층 1호 + 4
# 3층 3호 : 2층 1,2,3호 = 3층 2호 + 10

import sys

def fibo(k, n):
    f = [[0] * (n+1) for _ in range(k+1)] # k+1행 n+1열

    for i in range(n+1):
        f[0][i] = i
    for j in range(k+1):
        f[j][1] = 1
    for x in range(1, k+1):
        for y in range(1, n+1):
            f[x][y] = f[x][y-1] + f[x-1][y]
    return f[k][n]

for tc in range(1, int(sys.stdin.readline())+1):
    k = int(sys.stdin.readline()) # k : 층
    n = int(sys.stdin.readline()) # n : 호 에는 몇명이 살고있는가?
    print(fibo(k, n))
