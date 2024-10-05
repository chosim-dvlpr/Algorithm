import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    else:
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[0][1] + arr[1][0]
        dp[1][1] = arr[1][1] + arr[0][0]
        mx = max(dp[0][1], dp[1][1])

        for i in range(2, n):
            dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
            dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])

            mx = max(mx, dp[0][i], dp[1][i])
        
        print(mx)
    