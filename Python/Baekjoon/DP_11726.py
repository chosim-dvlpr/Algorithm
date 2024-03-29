# 2*1 : 1
# 2*2 : 2
# 2*3 : 3
# 2*4 : 5

n = int(input())
dp = [0]*(n+1)
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n]%10007)