# 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        print(arr[x1-1][y1-1])
    else:
        res = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        print(res)