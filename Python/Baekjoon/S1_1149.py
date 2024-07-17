# 1 ~ n번 집
# 빨/초/파 색칠하기 - 비용O
# 모든 집을 칠하는 비용의 최솟값
# 옆집과 색이 달라야 한다
# 비용
# 빨 초 파



import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * 3 for _ in range(n)]
for i in range(3):
    arr[0][i] = cost[0][i]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            arr[i][j] = min([cost[i][j] + arr[i-1][1], cost[i][j] + arr[i-1][2]])
        elif j == 1:
            arr[i][j] = min([cost[i][j] + arr[i-1][0], cost[i][j] + arr[i-1][2]])
        else:
            arr[i][j] = min([cost[i][j] + arr[i-1][0], cost[i][j] + arr[i-1][1]])
print(min(arr[-1]))
        