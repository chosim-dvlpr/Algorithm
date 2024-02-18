import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 네 자릿 수

for _ in range(n):
    A, B = map(int, input().split())
    visited = [False for i in range(10001)] # 방문한 숫자는 건너뛰기
    q = deque()
    q.append([A, ''])
    visited[A] = True # 방문 표시

    while q:
        num, command = q.popleft()

        if num == B:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append([s, command + 'S'])

        l = num // 1000 + (num % 1000) * 10 # 123을 왼쪽으로 회전하면 1230이 된다
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000 # 123을 오른쪽으로 회전하면 3012가 된다
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])