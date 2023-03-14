'''
**시간 초과 해결**
Queue => deque 사용
input => sys.stdin 사용

input이 문자 하나라면 split으로 나누어도 오류가 나지 않음
'''

from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    lst = list(map(str, sys.stdin.readline().split()))
    if lst[0] == 'push':
        q.append(int(lst[1]))
    elif lst[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif lst[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif lst[0] == 'size':
        print(len(q))
    elif lst[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    else:
        if q:
            print(q.popleft())
        else:
            print(-1)
