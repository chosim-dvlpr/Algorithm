'''
주어지는 수들은 10,000보다 작은 수 => 카운팅 정렬
'''


import sys

n = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

cnt = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    cnt[num] += 1

i = 0
while i != len(cnt):
    if cnt[i] == 0:
        i += 1
        continue
    print(i)
    cnt[i] -= 1

