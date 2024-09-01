import sys
input = sys.stdin.readline

n = int(input())
scores = [0] + [int(input().strip()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1:
    print(scores[1])
else:
    dp[1] = scores[1]
    dp[2] = dp[1] + scores[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])
    print(dp[-1])
