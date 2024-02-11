# 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간이 더 빠르고, 끝나는 시간이 같다면 시작시간이 같은 것을 앞으로 오도록 정렬

cnt = 0
endTime = 0

for start, end in meetings:
    if endTime <= start: # 앞선 미팅의 끝나는 시간이 현재 미팅의 시작시간보다 앞선다면
        endTime = end
        cnt += 1
print(cnt)
