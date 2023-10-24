# 왼쪽 : n개
# 오른쪽 : m개 (0 < n <= m < 30)
# 다리는 서로 겹칠 수 없음
# 다리를 지을 수 있는 경우의 수

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    

