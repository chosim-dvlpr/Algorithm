import sys

S = int(sys.stdin.readline())
n = 1

# n의 총합이 S보다 작을 때까지 반복
while n * (n+1) / 2 <= S:
    n += 1
    # n을 1씩 증가시킴

# n이 +1 된 상태이므로, 결과에선 1을 뺌
print(n-1)
