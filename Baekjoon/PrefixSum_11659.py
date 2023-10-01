# n개의 수
# i번째 수부터 j번째 수까지 합을 구하기
# m : 합을 구해야 하는 횟수
import sys

n, m = map(int, sys.stdin.readline().split())

# 문제에서 i, j가 인덱스 + 1이므로 arr 앞에 0을 더해줌
arr = [0] + list(map(int, sys.stdin.readline().split()))

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
