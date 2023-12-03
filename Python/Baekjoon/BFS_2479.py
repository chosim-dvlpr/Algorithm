import sys
from collections import deque
input = sys.stdin.readline

def hamming():
    visited[s] = 1 # 시작번호 방문처리
    q = deque()
    q.append((s, str(s)))
    while q:
        num, code = q.popleft()
        if num == e: # 종료 지점일 때
            return code
        for i in range(1, n+1):
            cnt = 0
            if visited[i]:
                continue
            # 방문하지 않은 지점일 때 글자 순회
            for j in range(k):
                if arr[num][j] != arr[i][j]:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1:
                visited[i] = 1
                q.append((i, code + ' ' + str(i)))
    return -1

n, k = map(int, input().split())
arr = ['0'] + [input().strip() for _ in range(n)]
# arr : ['0', '000', '111', '010', '110', '001']
s, e = map(int, input().split())
visited = [0] * (n+1)
print(hamming())
