n = int(input())

INF = 9876543210
dp = [INF] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0: # 여기를 if로 하기 (elif로 하면 6배수가 if에서만 걸리고 다음으로 넘어가서 최솟값이 안구해짐)
        dp[i] = min(dp[i], dp[i//2]+1)        

print(dp[n])
