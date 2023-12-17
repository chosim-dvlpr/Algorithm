# 플로이드 워셜 : 시간복잡도 O(n**3)
# n은 100 이하
# 모든 경우의 수 확인

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# k : 중간 노드가 될 노드 번호
# k를 중심으로 i -> k -> j 경로가 있는지 확인
# 경로가 있다면 arr[i][j]를 1로 업데이트
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1
                
for i in arr:
    print(*i)
