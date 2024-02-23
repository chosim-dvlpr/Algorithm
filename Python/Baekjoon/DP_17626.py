import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    mn = 1e9
    for j in range(1, int(math.floor(i**0.5)) + 1):
        mn = min(mn, dp[i - j**2]) # i == j**2 일 때는 dp[0] (0) 이 됨
    dp.append(mn + 1)
print(dp[n])

'''
1 : dp[1]
2 : dp[1]*2
3 : dp[1]*3
4 : dp[4]
5 : dp[4] + dp[1]
6 : dp[4] + dp[2]
7 : dp[4] + dp[3]
8 : dp[4] + dp[4]
9 : dp[9]
10: dp[9] + dp[1]
11: dp[9] + dp[2]
12: dp[9] + dp[3]
13 : dp[9] + dp[4]
14 : dp[9] + dp[5]
15 : dp[9] + dp[6]
16 : dp[16]
17 : dp[16] + dp[1]
18 : dp[16] + dp[2]
19 : dp[16] + dp[3]
20 : dp[16] + dp[4]
21 : dp[16] + dp[5]

24 : dp[16] + dp[8]
'''