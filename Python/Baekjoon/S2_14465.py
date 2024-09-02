import sys
from collections import deque
input = sys.stdin.readline

n, k, b = map(int, input().split())
wrong = [int(input()) for _ in range(b)]
wrong_cnt = 0
cnt = 0
cntList = deque([])
mn = 10e9

# 시작이 고장난 신호등인 경우도 고려 - wrong_cnt는 0
for i in range(1, n+1):
    if i in wrong:
        wrong_cnt += 1
        cntList.append(cnt)
        cnt = 0
        continue
    cnt += 1

    if cnt + sum(cntList) + wrong_cnt >= k:
        mn = min(mn, wrong_cnt)
        if cntList:
            cntList.popleft()
        wrong_cnt -= 1

    # print(mn)

print(mn)


