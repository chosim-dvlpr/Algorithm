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

def bfs(idx):
    for i in range(idx, n+1):
        if not picked[i]:
            picked[i] = 1
            print(picked, i)
bfs(1)
