# 단지수 출력
# 단지내 집의 수를 오름차순 정렬 -> 한 줄에 하나씩 출력

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().strip())) for _ in range(n))
countList = []
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            count = 1
            start = [i, j]
            arr[i][j] = 0
            q = deque([start])

            while q:
                [x, y] = q.popleft()

                for [dx, dy] in delta:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and arr[nx][ny] != 0:
                        count += 1
                        arr[nx][ny] = 0
                        q.append([nx, ny])
            countList.append(count)
countList.sort()
print(len(countList))
for c in countList:
    print(c)

    