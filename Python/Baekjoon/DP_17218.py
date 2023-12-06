import sys

st1 = sys.stdin.readline().strip()
st2 = sys.stdin.readline().strip()

len1 = len(st1)
len2 = len(st2)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(len1):
    for j in range(len2):
        if st1[i] == st2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            continue
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

res = ''
while dp[len1][len2] != 0:
    if dp[len1][len2] == dp[len1-1][len2]:
        len1 -= 1
        continue
    elif dp[len1][len2] == dp[len1][len2-1]:
        len2 -= 1
        continue
    res += st1[len1-1]
    len1 -= 1
    len2 -= 1

print(res[::-1])