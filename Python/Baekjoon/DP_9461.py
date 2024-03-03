import sys
input = sys.stdin.readline

tc = int(input())
dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
j = 1
for i in range(6, 101):
    dp[i] = dp[j] + dp[i-1]
    j += 1

for _ in range(tc):
    n = int(input())
    print(dp[n])
