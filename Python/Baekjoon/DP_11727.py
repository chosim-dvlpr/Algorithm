n = int(input())
dp = [0]*(n+1)
# n 분리하지 않으면 n == 1일 때 인덱스 에러 (런타임 에러)
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp[1] = 1
    dp[2] = 3
    # dp[3] = 2*3-1 = 5
    # 전부 세로로 세운 경우 중복 발생 => -1

    for i in range(3, n+1):
        dp[i] = dp[i-2]*2 + dp[i-1]

    print(dp[n]%10007)
