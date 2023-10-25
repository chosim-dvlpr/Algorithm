# 왼쪽 : n개
# 오른쪽 : m개 (0 < n <= m < 30)
# 다리는 서로 겹칠 수 없음
# 다리를 지을 수 있는 경우의 수

# 서쪽 1개, 동쪽 n개 => 다리 n개
# 서쪽 == 동쪽 => 다래 1개
# 서쪽 n개, 동쪽 m개 => 
    # 서쪽 n개, 동쪽 m-1개일 때와
    # 서쪽 n-1개, 동쪽 m-1개일 때를 더하면 됨
    # 누적합 비슷
# 피보나치와 비슷
# 조합론

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 서쪽 첫 번째 다리
            if i == 1:
                dp[i][j] = j
                continue
            # 서쪽 다리가 첫 번째가 아니면서
            # 동쪽 다리와 번호가 같을 때 : 1가지 경우의 수만 존재
            elif i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    print(dp[n][m])