# n명의 사람
# 각 사람이 돈을 인출하는데 걸리는 시간 P
# 인원 배열 => 5!
# 누적합 구하기 => 최솟값 찾기
# 누적합이 현재 최솟값보다 크면 종료

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p = deque([0] + list(map(int, input().split()))) # 1~n번까지의 값
picked = [0 for _ in range(n+1)] # 해당 번호 선택했는지 여부

lst = []
mn = 9876543210



def bfs(chosen, picked):
    global mn
    if len(chosen) == n:
        # print(chosen)
        arr = [0] * n # 누적합
        arr[0] = chosen[0]
        for i in range(1, n):
            arr[i] = arr[i-1] + chosen[i]
        if arr[-1] < mn:
            mn = arr[-1]
            print('mn 업데이트 : ', mn)
        return
    
    for i in range(1, n+1):
        if not picked[i]:
            chosen.append(p[i])
            picked[i] = 1
            bfs(chosen, picked)
            picked[i] = 0
            chosen.pop()
bfs([], picked)

